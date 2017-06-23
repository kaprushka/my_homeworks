# -*- coding: cp1251 -*-
# получаем массив слов из файла
def getText(file_name):
    with open(file_name,'r') as f:
        text = f.read()
        f.close()
    text = text.replace('\n', ' ') 
    return text

#записываем результат
def writeWords(f, file_name, text):
        count = text.count('lex')
        f.write(file_name + '\t' + str(count) + '\r\n')       

import re
from os import listdir
from os.path import isfile, join
path = './news/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

pattern = re.compile("^([a-zA-Z]+)$")

fresult = open('result.txt', 'w')

for x in onlyfiles:
    file_name = './news/' + x
    text = getText(file_name)
    writeWords(fresult, file_name, text)

fresult.close()
