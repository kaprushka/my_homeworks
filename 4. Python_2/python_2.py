N = input('Введите число')
N = int(N, base=10)
i = 0
while i < N:
    a = input('Введите слово')
    if a == 'программирование':
        break
    print(a)
    i += 1
