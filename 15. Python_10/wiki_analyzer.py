# coding=utf-8

def getSphere(lang, text):
    # Ищем сферу детельности
    if lang == 'RU' or lang == 'Ru' or lang == 'rU' or lang == 'ru':
        first = text.find('<span class="no-wikidata" data-wikidata-property-id="P101">')
        if first == -1: return -1
        text = text[first + 59:text.find('</span>', first)]
    elif lang == 'EN' or lang == 'En' or lang == 'eN' or lang == 'en':
        first = text.find('<td class="category">')
        if first == -1: return -1
        text = text[first + 21:text.find('</td>', first)]
    else: return -2
    # Удаляем всё лишнее
    while text.find('<') != -1: text = text[:text.find('<')] + text[text.find('>') + 1:]
    return text

def openFile(filename):
    file = open(filename,'r', encoding = 'utf-8') # Открываем файл
    text = file.read() # Читаем содержимое
    file.close() # Закрываем файл
    return text

filename = input('Введите имя файла: ')
text = openFile(filename)
lang = input('Введите язык статьи (RU - русский, EN - английский): ')
sphere = getSphere(lang, text)
if sphere == -1: print('Что-то ничего не могу найти :с')
elif sphere == -2: print('Этот язык я пока не знаю :с')
else: print('Этот, вроде бы, великий ученый занимался такой научной сферой, как ' + sphere + '. Учись, студент!')

