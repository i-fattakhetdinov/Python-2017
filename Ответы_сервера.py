s = ''
f = open('input.txt', 'r')
d = [0 for i in range(4)]
for line in f:
    d[3] += 1
    s = line
    s = s.split('"')
    s = s[2]
    s = s.split(' ')
    s = s[1]
    s = int(s)
    if(s == 200):
        d[0] += 1
    elif (300 <= s <= 309):
        d[1] += 1
    elif (s != ''):
        d[2] += 1
for i in d:
    print(i, end=" ")
