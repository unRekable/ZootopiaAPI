"""
This script loads animal data from a JSON file and an HTML template,
merges the data into the template, and saves the result as an HTML file.
"""

from typing import Any, Dict, List

def serialize_animal(animal_obj: Dict[str, Any]) -> str:
    """
    Serializes an animal object into an HTML string for a list item.

    Args:
        animal_obj (Dict[str, Any]): A dictionary containing the animal's data.
                                     Expected keys: "name" (str),
                                     "characteristics" (Dict with optional "diet", "type"),
                                     "locations" (List[str]).

    Returns:
        str: An HTML string representing the animal as a list item.
    """
    output_parts = [
        '<li class="cards__item">',
        f'<div class="card__title">{animal_obj.get("name", "N/A")}</div>',
        '<p class="card__text">',
    ]

    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "N/A")
    locations_list = animal_obj.get("locations", [])
    location = locations_list[0] if locations_list else "N/A"
    animal_type = characteristics.get("type")

    output_parts.append(f'<strong>Diet:</strong> {diet}<br/>')
    output_parts.append(f'<strong>Location:</strong> {location}<br/>')

    if animal_type:
        output_parts.append(f'<strong>Type:</strong> {animal_type}<br/>')

    output_parts.extend(['</p>', '</li>'])
    return "\n".join(output_parts)


def build_all_animals_html(animals_list: List[Dict[str, Any]]) -> str:
    """
    Builds an HTML string for all animals by serializing each one.

    Args:
        animals_list (List[Dict[str, Any]]): A list of animal objects.

    Returns:
        str: A string containing HTML for all animals, concatenated.
    """
    all_animals_html_parts = []
    for animal_obj in animals_list:
        if isinstance(animal_obj, dict):
            all_animals_html_parts.append(serialize_animal(animal_obj))
        else:
            print(f"Warning: Skipping non-dictionary item in animals_data: {animal_obj}")
    return "\n".join(all_animals_html_parts)


def generate_html_file(template_filepath: str, animals_html_content: str, output_filepath: str) -> bool:
    """
    Generates the animals HTML file from the template and animal data.

    Args:
        template_filepath (str): Path to the HTML template file.
        animals_html_content (str): HTML string content for all animals.
        output_filepath (str): Path where the final HTML file will be saved.

    Returns:
        bool: True if the file was generated successfully, False otherwise.
    """
    try:
        with open(template_filepath, 'r', encoding="utf-8") as template_file:
            html_template = template_file.read()
    except FileNotFoundError:
        print(f"Error: The template file {template_filepath} was not found.")
        return False

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html_content)

    try:
        with open(output_filepath, 'w', encoding="utf-8") as outfile:
            outfile.write(final_html)
        print(f"The file '{output_filepath}' was successfully created.")
        return True
    except IOError:
        print(f"Error: Could not write the file {output_filepath}.")
        return False