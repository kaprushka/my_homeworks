def getText(file_name):
    fsource = open(file_name,'r', encoding = 'utf-8')
    text = fsource.read()
    fsource.close()
    return text

def writeResult(file_name, text):
    fresult = open(file_name,'w', encoding = 'utf-8')    
    fresult.write(text)
    fresult.close()

fresult = open('res_1.txt','w', encoding = 'utf-8')

# Получим текст
text = getText('F.xml')

# Запишем результат
writeResult('res_1.txt', str(text[:text.index('</teiHeader>') + 12].count('\n') + 1))
