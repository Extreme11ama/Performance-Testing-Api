from locust import HttpUser, task, between
from dotenv import load
import random
import os

load()

Api_Key = os.getenv("OPENWEATHER_API_KEY")

class WeatherAPIUser(HttpUser):
    host = "https://api.openweathermap.org"
    wait_time = between(2, 5)

    @task(3)
    def get_current_weather_by_city(self):
        self.client.get(
            "/data/2.5/weather",
            params={
                "q": "Seattle",
                "appid": Api_Key,
                "units": "metric"
            },
            name="/weather [city]"
        )

    @task(3)
    def get_weather_different_cities(self):
        cities = ["New York", "Tokyo", "Paris", "Sydney", "Berlin"]
        city = random.choice(cities)
        self.client.get(
            "/data/2.5/weather",
            params={
                "q": city,
                "appid": Api_Key,
                "units": "metric"
            },
            name="/weather [random city]"
        )

    @task(2)
    def get_forecast(self):
        self.client.get(
            "/data/2.5/forecast",
            params={
                "q": "Seattle",
                "appid": Api_Key,
                "units": "metric"
            },
            name="/forecast"
        )

    @task(1)
    def get_weather_by_coordinates(self):
        self.client.get(
            "/data/2.5/weather",
            params={
                "lat": "47.2551",
                "lon": "122.4420",
                "appid": Api_Key,
                "units": "metric"
            },
            name="/weather [coordinates]"
        )