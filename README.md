# Weather Data Pipeline

Fetches hourly forecast data from the Open-Meteo Forecast API, transforms the
hourly arrays into database rows, and stores them in a local SQLite database.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

The default location is Chicago, Illinois. Override it with environment
variables:

```bash
WEATHER_LATITUDE=29.7604 WEATHER_LONGITUDE=-95.3698 WEATHER_TIMEZONE=America/Chicago python3 main.py
```

The pipeline writes to `weather.db`, which is ignored by Git.
