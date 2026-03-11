# Weather API Performance Testing

Simulated concurrent users hitting the OpenWeatherMap API 
to measure response time and identify rate limit thresholds.

## Tool
Locust (Python)

## Target
OpenWeatherMap REST API

## Endpoints Tested
- GET /weather — current weather by city name
- GET /weather — current weather by coordinates  
- GET /forecast — 5 day forecast

## Results

| Users | Avg Response Time | Requests/sec | Error Rate |
|-------|------------------|--------------|------------|
| 5     | 29.05            | 1.35         | 0          |
| 15    | 28.71            | 4.14         | 0          |
| 30    | 32.47            | 8.42         | 0          |

## Findings
The OpenWeatherMap API maintained consistent performance across all
tested load levels. Average response times remained stable between
~29–32 ms while scaling from 5 to 30 concurrent users.

Throughput increased proportionally with the number of users,
reaching approximately 8.4 requests per second at 30 users, indicating
the API handled the simulated load without noticeable degradation.

No HTTP errors or rate limiting responses were observed during the
test window, despite the documented free-tier limit of 60 requests
per minute. This may suggest the limit is enforced over longer
time windows or allows short bursts of traffic.

Additionally, the consistently low response times may indicate that
the API utilizes caching or CDN layers for frequently requested weather 
data, allowing repeated queries for the same city to be served quickly 
without hitting backend services.

## Setup
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Create a `.env` file with your OpenWeatherMap API key:
   `OPENWEATHER_API_KEY=your_key_here`
4. Run `locust` and open `http://localhost:8089`