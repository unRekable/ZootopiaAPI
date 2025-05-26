# Zootopia Animal Explorer

Welcome to Zootopia Animal Explorer! This project allows you to dynamically fetch information about various animals from an external API and display it neatly in an HTML file.

## Description

Zootopia is a Python-based tool that uses user input (e.g., an animal name) to retrieve data from the API-Ninjas Animals API. The fetched information is then processed and written to a local HTML page (`animals.html`), showcasing details about the found animals, including their name, diet, location, and type.

## Features

* Fetches real-time animal data based on user input.
* Utilizes the external [API-Ninjas Animals API](https://api-ninjas.com/api/animals).
* Automatically generates an HTML file to display animal information.
* Securely manages API keys using `.env` files.
* Modular code structure for easier maintenance and scalability.

## API Used

This project uses the **Animals API** by [API-Ninjas](https://api-ninjas.com/api/animals). You will need a personal API key to use their service.

## Prerequisites

* Python 3.7 or higher
* Pip (Python Package Installer)

## Setup and Installation

Follow these steps to set up the project locally:

1.  **Clone the Repository (Optional):**
    If you're downloading the project from a Git repository:
    ```bash
    git clone <repository-url>
    cd zootopia-project
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    * Windows: `venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`

3.  **Install Dependencies:**
    Create a file named `requirements.txt` in the root directory of your project with the following content:
    ```txt
    requests
    python-dotenv
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    * Sign up at [API-Ninjas](https://api-ninjas.com) to get your free personal API key for the "Animals API".
    * Create a file named `.env` in the root directory of your project.
    * Add your API key to the `.env` file like this:
        ```env
        API_KEY=YOUR_PERSONAL_API_KEY_HERE
        ```
        Replace `YOUR_PERSONAL_API_KEY_HERE` with the actual key you received from API-Ninjas.

## How to Run

To start the script:

1.  Ensure your virtual environment is activated and you are in the project's root directory.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  The script will prompt you to enter an animal name or search query.
4.  After your input, the script will fetch data from the API and generate/overwrite the `animals.html` file in the root directory with the retrieved animal information.
5.  Open `animals.html` in a web browser to view the results.

## Project Structure

```
zootopia-project/
├── .env                  # For API key (do not commit to version control!)
├── main.py               # Main script: handles user input and orchestration
├── api_client.py         # Module for API communication (contains fetch_data)
├── web_generator.py      # Module for HTML generation logic
├── template/
│   └── animals_template.html # HTML template
├── animals.html          # Generated HTML output file
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Troubleshooting

* **`Error: API_KEY not found.`**: Ensure the `.env` file is correctly created, contains the `API_KEY`, and is in the same directory from which you are running the script. Also, verify that `dotenv.load_dotenv()` is called at the beginning of your script that needs the API key (likely in `api_client.py` or `main.py` before the key is accessed).
* **HTTP errors (e.g., 401, 403)**: Double-check that your API key is correct and still valid. Free API keys often have usage limits.
* **No animals found**: The API might not have results for your specific query. Try a more general term or a different animal name.

---
