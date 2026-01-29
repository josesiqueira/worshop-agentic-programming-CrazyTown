r"""
Lesson 11: Pydantic AI agent framework - Extracting structured information from an image, in an agentic way with watch folder.
This time with 2 agents.
The first agent is doing the extraction of the structured information from the image.
The second agent is doing a web search for the genres of each band.

Do we need an agent 

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

# -- RUN WITH ANTHROPIC --

from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(  
    'anthropic:claude-haiku-4-5',
    instructions='Be concise, reply with one sentence.',  
)

result = agent.run_sync('Where does "hello world" come from?')  
print(result.output)

# -- RUN WITH OPENAI INSTEAD --

# from pydantic_ai import Agent
# from dotenv import load_dotenv

# load_dotenv()

# agent = Agent(  
#     'openai:gpt-5.2',
#     instructions='Be concise, reply with one sentence.',  
# )

# result = agent.run_sync('Where does "hello world" come from?')  
# print(result.output)