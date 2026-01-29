r"""
Lesson 4: Anthropic Responses API Without Tool Call

Setup:

Always create a virtual environment
1. python -m venv venv
2. source venv/bin/activate # On Windows use `venv\Scripts\activate`
3. deactivate # To exit the virtual environment

Install the dependencies
1. pip3 install anthropic
2. pip3 install dotenv

You can, however, install dependencies through pip freeze and a requirements.txt file:
1. pip3 freeze > requirements.txt
2. pip3 install -r requirements.txt
"""

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Where is Crazy Town in Tampere located?"}]
)

# What is this response?
#print(message)
print(response.model_dump_json(indent=2))

# What is the type of this response?
print(type(response))
# What is the message content?
#print(response.output_text)