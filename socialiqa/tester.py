import os
import openai
openai.api_type = "azure"
openai.api_base = "https://chatgpt-tom-experiment.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "9a17f809e62b445bb870e9f84803f009"

response = openai.Completion.create(
  engine="tom-davinci003",
  prompt="Hello",
  temperature=0.7,
  max_tokens=256,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=1,
  stop=None)
print(response)
