# Weather Data Pipeline

Fetches hourly forecast data from the Open-Meteo Forecast API, transforms the
hourly arrays into database rows, and stores them in Postgres.

## Setup

```bash
pip install -r requirements.txt
```

Start a local Postgres database:

```bash
docker compose up -d postgres
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

The default database connection is:

```text
postgresql://weather_user:weather_password@localhost:5432/weather_data
```

Override it with `DATABASE_URL` when needed.
