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

def promptfromdict(d,demos = 2):
    prompt = ''

    for i in range(demos):
        j = random.randint(0,len(pairs)-1)
        dd,a = pairs[j]
        prompt += getdemo(dd,a)
        prompt += '\n\n\n'


    prompt += d['context']+' '+d['question']
    prompt += '\nChoose one of the three options:'
    prompt += '\n(a) '+d['answerA']
    prompt += '\n(b) '+d['answerB']
    prompt += '\n(c) '+d['answerC']
    prompt += '\nYou must choose one of the options that is the most likely based on social common sense. Your Answer:'
    return prompt

f = open('dev.jsonl')
lines = f.readlines()
g = open('result.out','w+')
for line in tqdm(lines):
    d = json.loads(line)
    try:
        prompt = promptfromdict(d)
        out = getcompletion(prompt)
    except:
        print('bad!')
        out = ' (d) '
    #print(prompt)
    #break
    g.write(out)
    g.write('\n-----separator-----\n')

g.close()
f.close()

