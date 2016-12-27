import time
wordlist = []
word = input('Введите латинское слово: ')
while word:
    wordlist.append(word)
    word = input('Введите латинское слово: ')
for ind in wordlist:
    if ind.endswith('re') or ind.endswith('ri') or ind.endswith('isse'):
        print(ind)
time.sleep(5)
