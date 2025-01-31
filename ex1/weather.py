from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "api_key")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
async def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        }
    