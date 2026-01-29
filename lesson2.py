r"""
Lesson 2: Your First API Call with the OpenAI Python SDK - Chat Completions

%daqui
A Single Inference Call (Not an Agent)

This is a stateless, one-shot query to an LLM. The model receives a prompt,
generates a response, and forgets everything. There's no loop, no tools,
no memory—just a direct request-response pattern.

Key characteristics of a single inference call:
- One request → one response
- No memory between calls
- No tools or actions
- Reactive (answers only when asked)
- Stateless

This is NOT an AI agent. An agent would have:
- Temporal continuity (a loop running over time)
- Tools/actuators (search, database, filesystem, etc.)
- State/memory across steps
- Goal-directed behavior
% ate aqui, gerado por IA, pra eu colocar como explicação depois em alguma lesson futura.
---

Setup:

Always create a virtual environment
1. python -m venv venv
2. source venv/bin/activate # On Windows use `venv\Scripts\activate`
3. deactivate # To exit the virtual environment

Install the dependencies
1. pip3 install openai
2. pip3 install dotenv

You can, however, install dependencies through pip freeze and a requirements.txt file:
1. pip3 freeze > requirements.txt
2. pip3 install -r requirements.txt
"""

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {"role": "user", "content": "Where is Crazy Town in Tampere located?"}
    ]
)

# What is this response?
print(response)

# What is the type of this response?
print(type(response))

#What is the message content?
print(response.choices[0].message.content)

# What is this response message content?
#print(response.choices[0].message.content)

# Alternative way using the Responses API
# https://api.openai.com/v1/responses/{response_id}