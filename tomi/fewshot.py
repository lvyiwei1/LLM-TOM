import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion
def promptfromdict(q,elem):
    demos = [elem]
    while elem in demos:
        demos = random.sample(pairs,16)
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
for pp in tqdm(pairs):
    q,a,_ = pp
    prompt = promptfromdict(q,pp)
    try:
        g.write(getcompletion(prompt))
    except:
        g.write(' stupidazure ')
    g.write('\n-----separator-----\n')

g.close()
