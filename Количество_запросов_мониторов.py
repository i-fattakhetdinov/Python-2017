s = ''
f = open('input.txt', 'r')
result = 0
for line in f:
    s = line
    s = s.split('"')
    if(s[5] == 'Go-http-client/1.1'):
        result += 1
print(result)
