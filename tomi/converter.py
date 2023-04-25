import pandas as pd
df = pd.read_csv('tomi.csv')
pairs = []
for i,line :
    if i == 0:
        continue
    a = line.split(',')
    pairs.append((a[0]+' '+a[1],a[2],a[5]+'-'+a[8]+'-'+a[17]))
import torch
torch.save(pairs,'newpairs.pt')
