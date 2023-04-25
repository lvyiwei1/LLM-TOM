import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion
def promptfromdict(q):
    prompt = q
    prompt += '\nYou must answer in one word. Your answer is:'
    return prompt


import torch
pairs = torch.load('newpairs.pt')
g = open('result.out','w+')
for q,a,_ in tqdm(pairs):
    prompt = promptfromdict(q)
    print(prompt)
    exit(0)
    try:
        g.write(getcompletion(prompt))
    except:
        g.write(' stupidazure ')
    g.write('\n-----separator-----\n')

g.close()

