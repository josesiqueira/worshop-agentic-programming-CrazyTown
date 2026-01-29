r"""
Lesson 10: Pydantic AI agent framework - Extracting structured information from an image

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


# Problem : Do you think this is an agent?
# It is by definition not an agent, because it needs the 4 things in the instructions.md