from dotenv import load_dotenv
from fastapi import params
load_dotenv()

from anthropic import Anthropic
import os 


client = Anthropic()
model = "claude-haiku-5-5"


def add_user_message(messages, text):
    user_message = {"role":"user","content":text}
    messages.append(user_message)
    
def add_assistant_message(messages,text):
    assistant_message = {"role":"assistant","content":text}
    messages.append(assistant_message)


messages = []

add_user_message(messages, "write a 1 sentence description of a fake database")
# stream = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=messages,
#     stream=True,
# )

# for event in stream:
    
#     print(event)

with client.messages.stream(
    model=model,
    max_tokens=1200,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        # print(text, end="")
        pass
    
stream.get_final_message()