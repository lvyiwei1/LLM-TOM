import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion


ansdict = ['','(a)','(b)','(c)']
f1 = open('train.jsonl')
g1 = open('train-labels.lst')
pairs = []
for line,a in zip(f1.readlines(),g1.readlines()):
    d = json.loads(line)
    a = int(a)
    pairs.append((d,a))

def getdemo(d,a):
    prompt = 'Demonstration: \n'
    prompt += d['context']+' '+d['question']
    prompt += '\n(a) '+d['answerA']
    prompt += '\n(b) '+d['answerB']
    prompt += '\n(c) '+d['answerC']
    prompt += '\nCorrect Answer: '+ansdict[a]
    return prompt

def promptfromdict(d,ii,demos = 5):
    prompt = ''
    for i in range(demos):
        ind = distranks[ii].tolist().index(i)
        dd,a = pairs[ind]
        prompt += getdemo(dd,a)
        prompt += '\n\n\n'

    prompt += d['context']+' '+d['question']
    prompt += '\nChoose one of the three options:'
    prompt += '\n(a) '+d['answerA']
    prompt += '\n(b) '+d['answerB']
    prompt += '\n(c) '+d['answerC']
    prompt += '\nYou must choose one of the options that is the most likely based on social common sense. Your Answer:'
    return prompt

import torch
import numpy as np
def loadembeds(fn):
    a = torch.load(fn)
    return np.asarray(a)

embedstrain = loadembeds('embeds.pt')
embedsdev = loadembeds('embedsq.pt')
dists = 1 - np.matmul(embedsdev,embedstrain.T)
distranks = np.argsort(dists,axis=1)
f = open('dev.jsonl')
lines = f.readlines()
g = open('result.out','w+')
count = 0
for line in tqdm(lines):
    d = json.loads(line)
    try:
        prompt = promptfromdict(d,count)
        out = getcompletion(prompt)
    except:
        print('bad!')
        out = ' (d) '
    #print(prompt)
    #break
    g.write(out)
    g.write('\n-----separator-----\n')
    count += 1

g.close()
f.close()

