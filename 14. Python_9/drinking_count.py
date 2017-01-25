# coding=utf-8
import re

file = open('text.txt','r', encoding = 'utf-8')
text = file.read()
file.close()
# Невидовых форм глагола, причастий и деепричастий оказалось слиишком много (целых 24). На -ся нет форм
search_results = re.finditer("вып(и(ть|л.?|в(ш..?)?|т..)|ь(ют?|е(шь|м(те)?|те?))|ей(те)?)", text) 
words = []
print("В тексте найдены следущие формы слова 'выпить':")
for result in search_results:
    result = result.group()
    if words.count(result) == 0:
        words.append(result)
        print(result)
