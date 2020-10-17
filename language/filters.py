#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DE = {
    'a',
    'ab',
    'aber',
    'als',
    'am',
    'an',
    'auch',
    'auf',
    'aus',
    'bei',
    'beim',
    'bereits',
    'bis',
    'bislang',
    'da',
    'dabei',
    'dafür',
    'damit',
    'dann',
    'darf',
    'das',
    'dass',
    'dem',
    'den',
    'der',
    'deren',
    'des',
    'die',
    'diese',
    'dieser',
    'dieses',
    'doch',
    'dort',
    'durch',
    'ein',
    'eine',
    'einem',
    'einen',
    'einer',
    'eines',
    'er',
    'erneut',
    'erzählt',
    'erzählte',
    'erzählten',
    'es',
    'für',
    'gab',
    'gegeben',
    'gegen',
    'geht',
    'gesetzt',
    'gewesen',
    'gibt',
    'ging',
    'habe',
    'haben',
    'hat',
    'hatte',
    'hält',
    'heute',
    'hier',
    'ihm',
    'ihn',
    'ihnen',
    'ihr',
    'ihre',
    'ihrem',
    'ihren',
    'ihrer',
    'ihres',
    'im',
    'immer',
    'in',
    'innerhalb',
    'ins',
    'inzwischen',
    'ist',
    'jetzt',
    'kann',
    'kaum',
    'kein',
    'keine',
    'keinem',
    'keiner',
    'kommt',
    'können',
    'könnte',
    'könnten',
    'lassen',
    'machen',
    'mal',
    'man',
    'meine',
    'mit',
    'muss',
    'musste',
    'möglich',
    'müssen',
    'nach',
    'nicht',
    'noch',
    'nochmal',
    'nun',
    'nur',
    'ob',
    'oder',
    'sagte',
    'schon',
    'sei',
    'seien',
    'sein',
    'seine',
    'seinem',
    'seinen',
    'seiner',
    'seit',
    'sich',
    'sie',
    'sind',
    'so',
    'soll',
    'sollen',
    'sonst',
    'spricht',
    'steht',
    'trotz',
    'trotzdem',
    'tun',
    'um',
    'und',
    'viel',
    'vom',
    'von',
    'vor',
    'war',
    'warum',
    'was',
    'wegen',
    'weiter',
    'weitere',
    'wer',
    'werden',
    'wie',
    'wieder',
    'will',
    'wird',
    'wohin',
    'wollen',
    'wollte',
    'worden',
    'wurde',
    'wurden',
    'während',
    'würden',
    'x',
    'zu',
    'zum',
    'zur',
    'zwischen',
    'über',
}

LANGUAGES = {}
LANGUAGES['DE'] = DE

NON_WORD_CHARACTERS = [':', ',', '.', '!', '?', '-', '"', '&', '–', '„', '“', '(', ')', '\n', '\t']

def normalize(word, lang='DE'):
    w = word.lower()
    for non_word_char in NON_WORD_CHARACTERS:
        w = w.replace(non_word_char, '')
    w = w.strip()
    if w not in LANGUAGES[lang]:
        return w
    return ''
