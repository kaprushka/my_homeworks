marks = ['.', ',', '!', '?', ':', ';', '“', '”'] # какие знаки препинания могут быть в конце слова

# получить "слово" во мн.ч.
def words(count):
    # если последняя цифра от 1 до 4, а предпоследняя не 1, то вывести окончание "слова", иначе "слов"
    return 'слова' if (count % 10 > 0) and (count % 10 < 5) and (count // 10 % 10 != 1) else 'слов'

# получаем массив слов из файла
file_name = input('Введите имя файла: ')
with open(file_name,'r', encoding = 'utf-8') as f: 
    text = f.read() 
    text = text.replace('\n', ' ') 
    words_list = text.split(' ')

ed = 0
y = 0
e = 0
for word in words_list:
    # удаляем знак препинания
    while (len(word) > 0) and (marks.count(word[-1]) > 0): word = word[:-1]
    # если слово из одного или двух символов, то оно точно не на ed, так что идем далее
    if len(word) < 3: continue
    # определяем 'ed'
    if (word[-2] == 'e') and (word[-1] == 'd'):
        ed += 1
        if (word[-3] == 'i'):
            y += 1
        else:
            e += 1

print(ed, words(ed) + ' заканчивающихся на -ed. Из них:')
print('1.', y, words(y) + ' от слов на -y')
print('2.', e, words(e) + ' от слов на -e')
