import re

def getText(file_name):
    fsource = open(file_name,'r', encoding = 'utf-8')
    text = fsource.read()
    fsource.close()
    return text

def writeTypes(file_name, types):
    fresult = open(file_name,'w', encoding = 'utf-8')    
    for type_text in types:
        fresult.write(type_text + ': ' + str(types[type_text]) + '\n')
    fresult.close()

def writePronouns(file_name, pronouns):
    fresult = open(file_name,'a', encoding = 'utf-8')
    text = ''
    for word in words:
        text += word + ', '
    text = text[:-2]
    fresult.write(text)
    fresult.close()

def findTypes(text):
    types = dict()
    result = re.finditer('<w lemma=[^>]*>[^<]*</w>', text)
    for match in result:
        match_text = match.group()
        type_text = match_text[match_text.index('type="') + 6: match_text.index('">')]
        word = match_text[match_text.index('>') + 1: match_text.index('</')]
        if type_text in types:
            types[type_text] += 1
        else:
            types[type_text] = 1
    return types

def findPronoun(text):
    words = []
    result = re.finditer('<w lemma=[^>]*>[^<]*</w>', text)
    for match in result:
        match_text = match.group()
        type_text = match_text[match_text.index('type="') + 6: match_text.index('">')]
        word = match_text[match_text.index('>') + 1: match_text.index('</')]
        if type_text[0] == 'f' and type_text[2] == 'h':
            words.append(word)
    return words
        

# Получим текст
text = getText('F.xml')

# Найдем кол-во вхождений для каждого типа
types = findTypes(text)

# Запишем результат
writeTypes('res_2.txt', types)

words = findPronoun(text)

writePronouns('res_2.txt', words)
