#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import time

import language.filters as lf

DATE_FORMAT = '%Y-%m-%d'

NEW_FOR_DAYS = 14
CLEANUP_AFTER_DAYS = 90 # not seen in last 3 months
class Word(object):
    def __init__(self, word, link=None, usage_count=1, first=None, last=None):
        self.word = word
        self.usage_count = usage_count
        self.links = [link] if link else []
        now = _now_date()
        self._now = now
        self.first = first or now
        self.last = last or now
    def add_occurrence(self, link):
        self.usage_count += 1
        self.last = _now_date()
        if link not in self.links:
            self.links.append(link)
    def is_new(self):
        first = datetime.strptime(self.first, DATE_FORMAT)
        last = datetime.strptime(self.last, DATE_FORMAT)
        return (last - first).days <= NEW_FOR_DAYS
    def is_old(self):
        last = datetime.strptime(self.last, DATE_FORMAT)
        now = datetime.strptime(self._now, DATE_FORMAT)
        days_since_last_seen = (now - last).days
        return days_since_last_seen > NEW_FOR_DAYS
    def is_obsolete(self):
        last = datetime.strptime(self.last, DATE_FORMAT)
        now = datetime.strptime(self._now, DATE_FORMAT)
        return (now - last).days > CLEANUP_AFTER_DAYS
    def _as_json_snippet(self):
        if len(lf.normalize(self.word)) and not self.is_obsolete():
            return '"%s": {"first": "%s", "last": "%s"},' % (self.word, self.first, self.last)
        return ''
    def __str__(self):
        return f'({self.word}, {self.usage_count})'
    def __repr__(self):
        return str(self)

class WordDB(object):
    def __init__(self, words_json=None):
        self.words = words_json or {}
        for word in self.words.keys():
            w = self.words[word]
            self.words[word] = Word(word, None, 0, w['first'], w['last'])
    def add_words(self, text, link):
        words = text.split(' ')
        for word in words:
            w = lf.normalize(word)
            if len(w):
                if w in self.words.keys():
                    self.words[w].add_occurrence(link)
                else:
                    self.words[w] = Word(w, link)
    def words_by_usage(self):
        words = self.words.values()
        words = sorted(words, reverse=True, key=lambda w: w.usage_count)
        return list(words)
    def old_words(self):
        return [word for word in self.words.values() if word.is_old()]
    def as_json(self):
        '''Sorted & pretty printed, SCM-friendly
        '''
        buf = ['{']
        keys = sorted(self.words.keys())
        word_count = len(keys)
        for i in range(word_count):
            key = keys[i]
            json = self.words[key]._as_json_snippet()
            if len(json):
                buf.append(json)
        buf = '\n'.join(buf)
        # For last word, we omit the trailing comma to form valid json
        if buf[-1] == ',':
            buf = buf[:-1]
        return buf + '\n}\n'

def _now_date():
    return time.strftime(DATE_FORMAT, time.gmtime())

def worddb_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
        return WordDB(data)
    return WordDB()
