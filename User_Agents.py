s = ''
map = {'Windows': 0, 'Ubuntu': 0, 'OS X': 0, 'Unknown': 0}
f = open('input.txt', 'r')
for line in f:
    s = line
    s = s.split('"')
    if(s[5].find('Macintosh') != -1):
        map['OS X'] += 1
    elif(s[5].find('Windows') != -1):
        map['Windows'] += 1
    elif(s[5].find('Ubuntu') != -1):
        map['Ubuntu'] += 1
    else:
        map['Unknown'] += 1
for k, v in sorted(map.items(), key=lambda x: x[1]):
    print("%s: %s" % (k, v))
