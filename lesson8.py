r"""
Lesson 8: Structured information retrieval with OpenAI + Pydantic BaseModel

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
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

if not os.getenv('OPENAI_API_KEY'):
    raise RuntimeError('OPENAI_API_KEY not set; check the .env file.')

class Movie(BaseModel):
    title: str
    year: int

class MovieList(BaseModel):
    movies: list[Movie]

client = OpenAI()

response = client.responses.parse(
    model="gpt-5.2",
    input="What are 5 Finnish movies and their years?",
    text_format=MovieList
)

movies = response.output_parsed

print("Movies:")
for movie in movies.movies:
    print(f"  {movie.title} ({movie.year})")

# Problem : What if you need to change the Model?


# CHANGE THIS TASK
# After that: Homework - imporove what you created to retrieve the top 5 ranked movies in the imdb and then include the web search to search only in imdb website.

# After that: Task - imporove what you created to retrieve the top 5 ranked movies in the imdb and then include the web search to search only in imdb website.