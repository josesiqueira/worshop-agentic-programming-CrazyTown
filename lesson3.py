r"""
Lesson 3: OpenAI Responses API with Tool Calls

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

response = client.responses.create(
    model="gpt-5.2",
    tools=[{"type": "web_search"}],
    input="Where is Crazy Town in Tampere located?"
)


# What is this response?
#print(response)

# Let's print the full response in JSON format
print(response.model_dump_json(indent=2))

# What is the type of this response?
print("response type:")
print(type(response))

# What is just the message content?
print("response.output_text:")
print(response.output_text)

# How do I say to access whatever object inside this response method?
print("response.max_output_tokens:")
print(response.max_output_tokens)


# Alternative way using the Responses API
# https://api.openai.com/v1/responses/{response_id}

# You need to pass the response ID from the previous response
response_id = response.id

print("response_id:")
print(response_id)

# curl https://api.openai.com/v1/responses/{response_id} \
#   -H "Authorization: Bearer YOUR_OPENAI_API_KEY"

