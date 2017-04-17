import re
from os import listdir
from os.path import isfile, join
path = '.'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

pattern = re.compile("^([a-zA-Z]+)$")

ans = []

for x in onlyfiles:
	s = x.split('.')
	if len(s)<=2:
		if pattern.match(s[0]): ans.append(s[0])

print(' '.join(ans))
