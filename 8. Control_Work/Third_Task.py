k = 0
words = []
word = input()
while word:
    words.append(word)
    k+=1
    word = input()

with open('quotes.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    quotes = text.split('\n')

for word in words: 
    k = 0
    print("Слово '", word, "'")
    for quote in quotes:
        quote = quote.split(' — ');
        if " " + word in quote[0] or word + " " in quote[0]: # Обход ситуаций, когда слово находиться внутри другого слова. Напрмер слово "тест" в слове "сверхъестественное" 
            k += 1
            print(quote[0], '—', quote[1])
    if k == 0: 
        print("Нет цитат, где есть такое слово :с")
