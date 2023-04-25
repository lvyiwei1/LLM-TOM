import json
from tqdm import tqdm
import random
from OpenAIAPI import getcompletion
def promptfromdict(q):
    prompt = user_template
    qq = q.split('.')[-1][1:]
    story = q[:-len(qq)]
    prompt = prompt.replace('{question}',qq)
    prompt = prompt.replace('{story}',story)
    return prompt

user_template = """
Story:
{story}

Hint: The story is told according to the temporal order. You should reason the story line by line. For each line, you should think about each person's belief about the object's location. 
For example:
line xx: [story sentence]
[person1] knows [object] in [place], [person2] knows [object] in [place],
[person1] knows [person2] knows [object] in [place]
[person2]  knows [person1] knows [object] in [place]

Remember, a person can only have a belief about an object's last location when he is in the same room as the object. If he is in the same room, he is aware of any location changes made by others on the object until he leaves. If he is out of the room, he should not be aware of any new location changes made by others on the objects. If he comes back to the room, he only has a memory about the last location of the object when he was in the room before, and he can only update his knowledge when other people change the object's location after he comes back, he will not "actively" search and find out the object change when he was leaving.  Most importantly, everyone knows that one can not "actively"  search and find out the object change when he is out.

After you finish your reasoning, then answer the following questions:
Question: {question} 

Let's think step by step. First, you should think about the story line by line. For each line, you should think about each person's belief about the object's location.
Your final answer is:
"""


import torch
pairs = torch.load('newpairs.pt')
g = open('resultcot.out','w+')
for q,a,_ in tqdm(pairs[0:500]):
    prompt = promptfromdict(q)
    try:
        g.write(getcompletion(prompt))
    except:
        g.write(' stupidazure ')
    g.write('\n-----separator-----\n')

g.close()

