f = open('resultcot.out')
import torch
pairs = torch.load('newpairs.pt')
lines = f.read().split('\n-----separator-----\n')
corrects = {'all':0}
totals = {'all':0}
for i,p in enumerate(pairs[0:500]):
    label = p[2]
    if label not in corrects:
        corrects[label] = 0
    if label not in totals:
        totals[label] = 0
    if p[1].lower() in lines[i].lower(): 
        corrects[label] += 1
        corrects['all'] += 1
    totals[label] += 1
    totals['all'] += 1

out = {'corrects':corrects,'totals':totals}
print(out)

