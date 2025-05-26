from typing import Any, Dict, List
from api_client import fetch_data
from web_generator import build_all_animals_html, generate_html_file


# Constants for filenames
ANIMALS_TEMPLATE_FILE = 'template/animals_template.html'
OUTPUT_HTML_FILE = 'animals.html'


def main() -> None:
    """
    Main function of the script.
    Loads data, processes it, and writes the output HTML file.
    """

    animal_name = input('Enter a name of an animal: ')

    animals_data = fetch_data(animal_name)

    if not animals_data:
        print(f"The script will terminate, the animal {animal_name} was not found.")
        generate_html_file(ANIMALS_TEMPLATE_FILE, f'<div class="cards__item"><h2>The animal "{animal_name}" doesn\'t exist.</h2></div>', OUTPUT_HTML_FILE)
        return

    if not isinstance(animals_data, list):
        print(f"Warning: Expected a list of animals, but got {type(animals_data)}. Cannot process.")
        print("The script will terminate.")
        return

    all_animals_html_str = build_all_animals_html(animals_data)

    success = generate_html_file(ANIMALS_TEMPLATE_FILE, all_animals_html_str, OUTPUT_HTML_FILE)

    if not success:
        print("The script terminated due to an error generating the HTML file.")


if __name__ == "__main__":
    main()