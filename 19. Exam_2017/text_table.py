import os 

def text_read(): 
    path = '{}\\news'.format(os.getcwd()) 
    cout = 0 
    for f in os.listdir(path): 
        o = open('{}\\{}'.format(path, f), 'r+') 
        for line in o: 
            if 'w' in line: 
                cout += 1 
        sf = open('slova.txt', 'a+') 
        sf.write('{}\t{}\n'.format(f, cout)) 
        cout = 0 

def table(): 
    path = '{}\\news'.format(os.getcwd()) 
    sv = open('table.csv', 'a+') 
    sv.write('Название файла,Автор,Дата создания текста\n') 
    for f in os.listdir(path): 
        o = open('{}\\{}'.format(path, f), 'r+') 
        sv.write('{},'.format(f)) 
        for line in o: 
            if 'author' in line: 
                sv.write('{},'.format(line[line.index('=')+1:line.index('name')].replace('"', '').strip())) 
            if 'created' in line: 
                sv.write('{}\n'.format(line[line.index('=')+1:line.index('name')].replace('"', '').strip())) 

def result(): 
    text_read() 
    print() 
    table() 

if __name__ == '__result__': 
    result()
