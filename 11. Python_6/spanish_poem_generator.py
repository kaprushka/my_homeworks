# coding=utf-8
import random

def verb(syllables):
    # эта функция возвращает случайный глагол с нужным кол-вом слогов
    file = open('verbs_' + syllables + '.txt','r', encoding = 'utf-8')
    text = file.read()
    verbs = text.split('\n')
    return random.choice(verbs)
    
def noun(syllables):
    # эта функция возвращает случайное существительное с нужным кол-вом слогов
    file = open('nouns_' + syllables + '.txt','r', encoding = 'utf-8')
    text = file.read()
    nouns = text.split('\n')
    return random.choice(nouns)

def punctuation():
    # эта функция возвращает случайный знак препинания
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verse_5():
    # эта функция собирает строчку из 5 слогов
    return noun('3') + ' ' + verb('2') + punctuation()

def verse_7():
    # эта функция собирает строчку из 7 слогов
    return noun('5') + ' ' + verb('2') + punctuation()

def make_poem():
    return verse_5() + '\n' + verse_7() + '\n' + verse_5()

print(make_poem())


