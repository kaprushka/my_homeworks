word = input('Введите слово: ')
for i in word:
    print(word)
    word = word[-1] + word[:-1]
