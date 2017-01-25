# coding=utf-8
import random
import csv

csv_file = open("words.csv",'r', encoding = 'utf-8') # Открываем файл
words = [row for row in csv.reader(csv_file)] # Читаем csv файл в список для удобной работы
csv_file.close() # Закрываем файл
while True:
    word = words[random.randint(0, len(words) - 1)] # Выбираем случайное слово
    print("\nПосмотрим, сможете ли Вы догадаться, что пропущено в этом словосочетании:\n" + word[1]) # Печатаем подсказку
    user_word = input("Как Вы думаете, что же это?\n> ") # Спрашиваем у пользователя слово
    if user_word == word[0]: # Сравниваем полученное слово с ответом
        print("Совершенно верно! Так держать!")
    else:
        print("К сожалению, это неправильный ответ :с\nТам больше подходит слово '" + word[0] + "'")
    repeat = input("Может хотите попробовать ещё раз? Если нет то так и скажите!\n> ")
    if repeat == "Нет" or repeat == "нет" or repeat == "Не хочу" or repeat == "не хочу": # Если пользователь больше не хочет, то выходим
        break

