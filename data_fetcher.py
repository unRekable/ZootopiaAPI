import os

import requests, dotenv
from typing import Any, Dict, List

dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')
ANIMALS_API_URL = 'https://api.api-ninjas.com/v1/animals?name='

def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """

    resp = requests.get(ANIMALS_API_URL + animal_name, headers={'X-Api-Key': API_KEY})
    return resp.json()