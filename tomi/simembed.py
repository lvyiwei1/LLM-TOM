import json
from tqdm import tqdm
import random
from OpenAIAPIembed import getembedding
import time



import torch
pairs = torch.load('newpairs.pt')
#embeds = []
embeds = torch.load('newembeds.pt')
count = -1
for d,_,_ in tqdm(pairs):
    count += 1
    if count < len(embeds):
        continue
    
    prompt = d
    embed = getembedding(prompt)
    embeds.append(embed)
    torch.save(embeds,'newembeds.pt')
    time.sleep(0.95)


