#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DE = {
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
    'dabei',
    'damit',
    'dann',
    'darf',
    'das',
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
    'erzählte',
    'es',
    'für',
    'gegeben',
    'geht',
    'gesetzt',
    'gewesen',
    'ging',
    'habe',
    'haben',
    'hat',
    'hatte',
    'heute',
    'ihm',
    'ihn',
    'ihr',
    'ihre',
    'ihrem',
    'ihren',
    'ihrer',
    'im',
    'immer',
    'in',
    'innerhalb',
    'ins',
    'ist',
    'jetzt',
    'kann',
    'kaum',
    'kommt',
    'können',
    'könnte',
    'lassen',
    'mal',
    'man',
    'meine',
    'mit',
    'muss',
    'musste',
    'nach',
    'nicht',
    'noch',
    'nun',
    'nur',
    'ob',
    'oder',
    'sagte',
    'schon',
    'sei',
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
    'sonst',
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
    'was',
    'weiter',
    'weitere',
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
    'während',
    'würden',
    'zu',
    'zum',
    'zur',
    'zwischen',
    'über',
}

LANGUAGES = {}
LANGUAGES['DE'] = DE

NON_WORD_CHARACTERS = [':', ',', '.', '!', '?', '-', '"', '&']

def normalize(word, lang='DE'):
    w = word.lower()
    for non_word_char in NON_WORD_CHARACTERS:
        w = w.replace(non_word_char, '')
    w = w.strip()
    if w not in LANGUAGES[lang]:
        return w
    return ''
