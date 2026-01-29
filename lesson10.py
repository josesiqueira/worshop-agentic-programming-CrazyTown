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

from pathlib import Path
from pydantic import BaseModel
from pydantic_ai import Agent, BinaryContent
from dotenv import load_dotenv

load_dotenv()


class Concert(BaseModel):
    venue: str
    location: str
    date: str
    event_name: str | None


class BandInfo(BaseModel):
    band_name: str
    concerts: list[Concert]


class ConcertExtraction(BaseModel):
    bands: list[BandInfo]


def get_media_type(filepath: Path) -> str:
    """Get the MIME type based on file extension"""
    suffix = filepath.suffix.lower()
    media_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
    }
    return media_types.get(suffix, 'image/jpeg')


folder = Path("images")

if not folder.exists():
    raise FileNotFoundError(f"Folder '{folder}' not found")

# Collect all results
all_bands: dict[str, list[Concert]] = {}
"""
Process all images in the folder and return a dict where:
- key = band name
- value = list of Concert objects (venue, location, date, event_name)
"""

# Supported image extensions
image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

for image_path in folder.iterdir():
    if image_path.suffix.lower() not in image_extensions:
        continue
        
    print(f"Processing: {image_path.name}")
    
    # Read image and send to agent
    image_data = image_path.read_bytes()
    media_type = get_media_type(image_path)

    agent = Agent(
    'openai:gpt-5.2',
    output_type=ConcertExtraction,
    instructions="""
    Extract concert information from the image.
    For each band visible, extract:
    - The band name
    - The venue(s) where they play
    - The location of each venue
    - The date of each concert
    - The event/festival name (if it's part of a named event like a festival)
    If any information is unclear or missing, use "Unknown" as the value.
    Leave event_name as null if there's no specific event/festival name.
    """,
)
    
    result = agent.run_sync([
        "Extract all concert information from this image.",
        BinaryContent(data=image_data, media_type=media_type),
    ])
    
    # Merge results into our dictionary
    for band_info in result.output.bands:
        if band_info.band_name not in all_bands:
            all_bands[band_info.band_name] = []
        all_bands[band_info.band_name].extend(band_info.concerts)

# Pretty print results
for band, concerts in all_bands.items():
    print(f"\nBand: {band}")
    for concert in concerts:
        event_str = f" ({concert.event_name})" if concert.event_name else ""
        print(f"   Venue: {concert.venue} - {concert.location}{event_str}")
        print(f"   Date: {concert.date}")
