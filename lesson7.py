r"""
Lesson 7: Structured information retrieval with OpenAI

Setup:

Always create a virtual environment
1. python -m venv venv
2. source venv/bin/activate # On Windows use `venv\Scripts\activate`
3. deactivate # To exit the virtual environment

Install the dependencies
1. pip3 install pydantic_ai
2. pip3 install dotenv

You can, however, install dependencies through pip freeze and a requirements.txt file:
1. pip3 freeze > requirements.txt
2. pip3 install -r requirements.txt
"""
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if not os.getenv('OPENAI_API_KEY'):
    raise RuntimeError('OPENAI_API_KEY not set; check the .env file.')

client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="What are 5 Finnish movies and their years?",
    text={
        "format": {
            "type": "json_schema",
            "name": "movie_list",
            "schema": {
                "type": "object",
                "properties": {
                    "movies": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "year": {"type": "integer"}
                            },
                            "required": ["title", "year"],
                            "additionalProperties": False
                        }
                    }
                },
                "required": ["movies"],
                "additionalProperties": False
            }
        }
    }
)

print("printing response:")
print(response)

print("parsed output:")
parsed = json.loads(response.output_text)
print(parsed)

print("Movies:")
for movie in parsed["movies"]:
    print(f"  {movie['title']} ({movie['year']})")

print("\nUsage:", response.usage)

# First problem, difficult to maintain the JSON schema.

# Now let's make the JSON more maintanable by using pydantic BaseModel

# Another problem: Everytime you run this, the output may vary.
