# coding=utf-8
import re

file = open('text.txt','r', encoding = 'utf-8')
text = file.read()
file.close()
# Невидовых форм глагола, причастий и деепричастий оказалось слиишком много (целых 24). На -ся нет форм
search_results = re.finditer("вып(и(ть|л.?|в(ш..?)?|т..)|ь(ют?|е(шь|м(те)?|те?))|ей(те)?)(\.|,|!|\?|:|;|“|”|\"|\'|\(|\)|«|»)*", text)
words = [] # найденные слова
marks = ['.', ',', '!', '?', ':', ';', '“', '”', "'", '"', '(', ')', '«', '»'] # какие знаки препинания моогут быть в конце слова
print("В тексте найдены следущие формы слова 'выпить':")
for result in search_results:
    result = result.group()
    while (marks.count(result[-1]) > 0): result = result[:-1] # удаляем знаки препинания
    if words.count(result) == 0:
        words.append(result)
        print(result)
