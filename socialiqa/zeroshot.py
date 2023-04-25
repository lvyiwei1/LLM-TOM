import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion
def promptfromdict(d):
    prompt = d['context']+' '+d['question']
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
    prompt = promptfromdict(d)
    try:
        g.write(getcompletion(prompt))
    except:
        g.write(' (d) ')
        print(prompt)

    g.write('\n-----separator-----\n')

g.close()
f.close()

