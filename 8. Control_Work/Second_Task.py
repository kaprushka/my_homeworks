with open('quotes.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    quotes = text.split('\n')

k = 0
authors = []
for quote in quotes:
    quote = quote.split(' — ');
    if "разум " in quote[0] or " разум" in quote[0]: # Обход ситуаций, когда слово находиться внутри другого слова. Напрмер слово "тест" в слове "сверхъестественное"
        k += 1
        authors.append(quote[1])

print(k, "цитат со словом 'разум'")
for author in authors[:-1]:
    print(author, end=", ")
print(authors[-1])
