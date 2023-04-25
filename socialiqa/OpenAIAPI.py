"""
import openai
openai.api_key = open('/home/yiweilyu/apikey.token').readlines()[0][:-1]
def getcompletion(prompt,engine = 'text-davinci-003',max_token=150):
    completion = openai.Completion.create(engine=engine,prompt=prompt,max_tokens=max_token,temperature=0)
    return completion.choices[0].text
"""


#"""
import openai
openai.api_type = "azure"
openai.api_base = "https://chatgpt-tom-experiment.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "9a17f809e62b445bb870e9f84803f009"
def getcompletion(prompt):
    completion = openai.Completion.create(engine='tom-davinci003',prompt=prompt,max_tokens=150,temperature=0,stop=None,best_of=1,frequency_penalty=0,presence_penalty=0,top_p=0.95)
    return completion.choices[0].text
#"""
