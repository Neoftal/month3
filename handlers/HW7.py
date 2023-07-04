import os
import openai
from decouple import config

openai.api_key = config("Key")

async def find(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["stop"]
  )
  return(response['choices'][0]['text'])