import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion



import torch
import numpy as np
def loadembeds(fn):
    a = torch.load(fn)
    return np.asarray(a)

embedsdev = loadembeds('newembeds.pt')
dists = 1 - np.matmul(embedsdev,embedsdev.T)
distranks = np.argsort(dists,axis=1)

def promptfromdict(q,ii,numdemos=16):
    demos = []
    for i in range(numdemos):
        rank = distranks[ii].tolist().index(i+1)
        demos.append(pairs[rank])
    prompt = ''
    for tq,ta,_ in demos:
        prompt += 'Demonstration:\n'
        prompt += tq
        prompt += '\nCorrect Answer: '+ta
        prompt += '\n\n\n'

    prompt += 'Now answer the following question based on common sense:\n'
    prompt += q
    prompt += '\nYou must answer in one word. Your answer is:'
    return prompt




import torch
pairs = torch.load('newpairs.pt')
g = open('result.out','w+')
for i,pp in tqdm(enumerate(pairs)):
    q,a,_ = pp
    prompt = promptfromdict(q,i)
    try:
        g.write(getcompletion(prompt))
    except:
        g.write(' stupidazure ')
    g.write('\n-----separator-----\n')

g.close()
