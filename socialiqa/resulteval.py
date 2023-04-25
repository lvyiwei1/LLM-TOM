f = open('result.out')
g = open('dev-labels.lst')
lines = f.read().split('\n-----separator-----\n')
reses = []
for line in lines[:-1]:
    if 'a)' in line: 
        reses.append(1)
    elif 'b)' in line: 
        reses.append(2)
    elif 'c)' in line:
        reses.append(3)
    else:
        reses.append(4)
anses = g.readlines()
print(len(reses))
corrects = 0
for i in range(len(reses)):
    if reses[i] == int(anses[i]):
        corrects += 1

print(corrects)

