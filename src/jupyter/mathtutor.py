from dotenv import load_dotenv
from fastapi import params
load_dotenv()

from anthropic import Anthropic
import os 


client = Anthropic()
# model = "claude-sonnet-5"
model = "claude-haiku-4-5-20251001"

def add_user_message(messages, text):
    user_message = {"role":"user","content":text}
    messages.append(user_message)
    
def add_assistant_message(messages,text):
    assistant_message = {"role":"assistant","content":text}
    messages.append(assistant_message)

def chat_with_claude(messages, system=None, temperature=1.0):
    params = {
      "model":model,
      "max_tokens":1200,
      "messages":messages,
    }

    if system:
      params["system"] = system

    
    response = client.messages.create(
        **params
    )

    return response.content[0].text

messages = []

system = """
    You are a math teacher and want to explain to the sutdent how to solve the maths probelm, 
    what you should do is explain the step by step solution to the problem and then explain to them 
    so that they understand the solution. you should also privide simpleistic and real world exaples to explain them the solution. 
"""

while True:
    user_input = input("User: ")
    add_user_message(messages, user_input)
    assistant_response = chat_with_claude(messages, system)
    add_assistant_message(messages, assistant_response)
    print("Claude: " + assistant_response)

