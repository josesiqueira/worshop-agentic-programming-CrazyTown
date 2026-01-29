r"""
Lesson 13: Pydantic AI agent framework - Interactive CSV Query Agent

A simple agent that answers questions about the concerts-async.csv file.
It reads the CSV data and can answer questions like:
- How many heavy metal bands are in this file?
- What bands are from Finland?
- List all genres in the database

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

import csv
from pathlib import Path

from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv

load_dotenv()

# Configuration
CSV_FILE = Path("concerts-async.csv")


def load_csv_data() -> str:
    if not CSV_FILE.exists():
        return "CSV file does not exist."
    
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    if not rows:
        return "The CSV file is empty."
    
    # Format data as a readable string
    lines = [f"CSV Data ({len(rows)} records):"]
    lines.append("Columns: " + ", ".join(rows[0].keys()))
    lines.append("-" * 50)
    
    for row in rows:
        lines.append(str(dict(row)))
    
    return "\n".join(lines)


# Create the query agent
query_agent = Agent(
    'openai:gpt-5.2',
    deps_type=str,  # The CSV data will be passed as dependency
    instructions="""
    You are a helpful assistant that answers questions about concert data.
    
    You have access to a CSV database containing information about bands, their genres, 
    countries of origin, concert venues, locations, and dates.
    
    The CSV columns are: timestamp, source_image, band_name, genre, country, venue, location, date, event_name
    
    Rules:
    - ONLY answer questions based on the data provided to you
    - If the information is not in the data, say "I don't have this information in the database"
    - Be precise and count carefully when asked about numbers
    - When listing items, format them nicely
    - Be concise but helpful
    """,
)


# Dynamic instructions decorator: Adds context to the agent at runtime.
# Unlike static instructions (passed to Agent constructor), this function
# is called before each run and can access dependencies via RunContext.
@query_agent.instructions
def add_csv_data(ctx: RunContext[str]) -> str:
    """Inject the CSV data into the agent's instructions at runtime"""
    return f"\n\nHere is the concert database:\n\n{ctx.deps}"


def main():
    # Load CSV data once at startup
    csv_data = load_csv_data()
    

    print("Query Agent of custom dataset")
    print(f"Loaded data from: {CSV_FILE}")
    print("Ask questions about the concert data. Type 'q' to exit.")

    
    while True:
        try:
            # Get user input
            question = input("You: ").strip()
            
            # Check for exit
            if question.lower() == 'q':
                print("Goodbye!")
                break
            
            # Skip empty input
            if not question:
                continue
            
            # Run the agent with the question
            result = query_agent.run_sync(question, deps=csv_data)
            
            print(f"\nAgent: {result.output}")
            print(f"[Tokens: {result.usage().input_tokens} in / {result.usage().output_tokens} out]\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main() 