import re

def getText(file_name):
    fsource = open(file_name,'r', encoding = 'utf-8')
    text = fsource.read()
    fsource.close()
    return text

def writeResult(file_name, types):
    fresult = open(file_name,'w', encoding = 'utf-8')    
    for type_text in types:
        fresult.write(type_text + ': ' + str(types[type_text]) + '\n')
    fresult.close()

def findTypes(text):
    types = dict()
    result = re.finditer('<w lemma=[^>]*>', text)
    for match in result:
        match_text = match.group()
        type_text = match_text[match_text.index('type="') + 6: match_text.index('">')]
        if type_text in types:
            types[type_text] += 1
        else:
            types[type_text] = 1
    return types

# Получим текст
text = getText('F.xml')

# Найдем кол-во вхождений для каждого типа
types = findTypes(text)

# Запишем результат
writeResult('res_2.txt', types)
