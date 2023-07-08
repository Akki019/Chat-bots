from bardapi import Bard
import json 

with open('credentials.json','r') as f:
    file = json.load(f)
    token = file['token']


bard = Bard(token=token)
response = bard.get_answer("What is data science?")['content']
print(response)