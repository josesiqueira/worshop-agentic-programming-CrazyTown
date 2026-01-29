r"""
Lesson 6: Anthropic Responses API with Tool Calls + Allowed domains and Location

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
    messages=[
        {"role": "user", "content": "Where is Crazy Town in Tampere located?"}
    ],
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5,
        "allowed_domains": ["crazytown.fi", "tampere.fi"],
        "user_location": {
            "type": "approximate",
            "city": "Tampere",
            "region": "Pirkanmaa",
            "country": "FI",
            "timezone": "Europe/Helsinki"
        }
    }]
)

# What is this response?
#print(message)
print("response:")
print(response.model_dump_json(indent=2))

# What is the type of this response?
print("response type:")
print(type(response))
# What is the message content?
#print(response.output_text)

# Extracting only the text blocks from the response content
final_message = ""
for block in response.content:
    if block.type == "text":
        final_message += block.text

print("Printing only the final message content:")
print(final_message)