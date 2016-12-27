mass = []
with open('text.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    text = text.replace('\n',' ')
    mass = text.split(' ')
k = 0
for slovo in mass:
    if (slovo[-1] != '.') and (slovo[-1] != ','):
        k += 1
slova = len(mass)
percent = k/slova * 100
print('Процент слов, не оканчивающихся на знак препинания, равен: ', percent, '%')
