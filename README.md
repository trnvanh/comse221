# Coding Exercise 1 - Weather Microservice
This coding exercise is a simple FastAPI-based microservice that fetches weather data for a given city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data for any city.
- Uses FastAPI.
- Returns temperature and weather description in JSON format.

## Prerequisites
- Python 3.7+
- OpenWeatherMap API key (get one at https://openweathermap.org/api)

## Installation
For Linus users
1. Clone the repo

git clone https://github.com/trnvanh/comse221.git

cd ex1

2. Create and activate a virtual environment

python3 -m venv myenv

source myenv/bin/activate

3. Install dependencies

pip install fastapi uvicorn httpx

4. Set up API key

export OPENWEATHER_API_KEY=your_api_key_here

## Running the microservice
Start the FastAPI server

uvicorn weather:app --reload

The service will be available at http://127.0.0.1:8000

## Usage
Get Weather for a city

Send a GET request 

http://127.0.0.1:8000/weather/{city}

For example:
- Open browser: http://127.0.0.1:8000/weather/London
- Using curl: curl -X GET "http://127.0.0.1:8000/weather/London"

Example respond

{"city":"London","temperature":7.01,"weather":"overcast clouds"}

## Testing
Using python

import requests

response = requests.get("http://127.0.0.1:8000/weather/London")

print(response.json())

## Deployment
Running with Docker
1. Build the Docker image

docker build -t weather

2. Run the container

docker run -p 8000:8000 -e OPENWEATHER_API_KEY=your_api_key_here weather

## License
This project is licensed under the MIT License
