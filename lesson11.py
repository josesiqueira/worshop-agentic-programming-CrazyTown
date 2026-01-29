r"""
Lesson 11: Pydantic AI agent framework - Extracting structured information from an image, in an agentic way with watch folder
Not using database, just a CSV file, it is appending at the end of the file, every time a new image is processed.

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
