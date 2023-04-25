import os
import openai
import numpy as np
openai.api_type = "azure"
openai.api_base = "https://chatgpt-tom-experiment.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "9a17f809e62b445bb870e9f84803f009"
def getembedding(inpu):
  response = openai.Embedding.create(
    engine="tom-embedding",
    input=inpu)
  return response['data'][0]['embedding']
