import re

import language.words as w

def test_read_worddb_from_file():
    db = w.worddb_from_file('test/example_worddb.json')
    assert db.words.keys() == set({'auto', 'welt', 'zeit'})
    assert db.words['zeit'].links == []
    assert db.words['zeit'].usage_count == 0
    assert db.words['zeit'].first == '2020-08-24'
    assert db.words['zeit'].last == '2020-09-01'

def test_word_as_json_snippet():
    word = w.Word('zeit', None, 0, '2020-08-15', '2020-09-01')
    assert word._as_json_snippet() == '"zeit": {"first": "2020-08-15", "last": "2020-09-01"},'

def test_worddb_as_json():
    worddb = w.WordDB()
    worddb.add_words('Brown wolf jumps', None)
    assert re.match(r'''{
"brown": {"first": "\d{4}-\d{2}-\d{2}", "last": "\d{4}-\d{2}-\d{2}"},
"jumps": {"first": "\d{4}-\d{2}-\d{2}", "last": "\d{4}-\d{2}-\d{2}"},
"wolf": {"first": "\d{4}-\d{2}-\d{2}", "last": "\d{4}-\d{2}-\d{2}"}
}''', worddb.as_json())

def test_now():
    date = w._now_date()
    assert re.match(r'\d{4}-\d{2}-\d{2}', date)
