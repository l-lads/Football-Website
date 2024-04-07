# Football Website

This is a Flask-based web application that showcases football (soccer) data and information.

## Prerequisites

1. Python 3.x
2. Virtual Environment (venv)
3. API account with [API-FOOTBALL](https://www.api-football.com/)

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/football-website.git
```

2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required packages
```
pip install -r requirements.txt
```
4. Obtain an API key from API-FOOTBALL:

Sign up for a free account or log in to your existing account.
Navigate to the "API" section and copy your API key.

5. Update the api.py file with your API key:
```
API_KEY = "your_api_key_here"
```

## Usage

1. Start the Flask development server:
```
flask run
```

2. Open your web browser and navigate to `http://localhost:5000` to access the Football Website.

## Features

Displays football (soccer) data and information using the API-FOOTBALL API.

Allows users to explore various aspects of the sport, such as teams, players, leagues, and more.

Provides a user-friendly interface for interacting with the data.

## License 

This project is licensed under the MIT License.