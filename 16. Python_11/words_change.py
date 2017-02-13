import re

fopen = open('phylosophy.txt', 'r', encoding='utf-8')
fresult = open('result.txt', 'w', encoding='utf-8')

string = fopen.read()

# Если есть есть "философ"
string = re.sub('Философия', 'Астрология', string)
string = re.sub('Философии', 'Астрологии', string)
string = re.sub('Философию', 'Астрологию', string)
string = re.sub('Философией', 'Астрологией', string)

string = re.sub('философия', 'астрология', string)
string = re.sub('философии', 'астрологии', string)
string = re.sub('философию', 'астрологию', string)
string = re.sub('философией', 'астрологией', string)

# Если нет слова "философ"
# string = re.sub('Философ', 'Астролог', string)
# string = re.sub('философ', 'астролог', string)

fresult.write(string)

fopen.close()
fresult.close()
