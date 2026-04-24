from __future__ import annotations

import os
from typing import Any

import requests


OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_HOURLY_VARIABLES = (
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
)


def fetch_weather(
    latitude: float | None = None,
    longitude: float | None = None,
    timezone: str | None = None,
    forecast_days: int = 7,
) -> dict[str, Any]:
    """Fetch hourly forecast data from Open-Meteo."""
    latitude = latitude if latitude is not None else _env_float("WEATHER_LATITUDE", 41.8781)
    longitude = longitude if longitude is not None else _env_float("WEATHER_LONGITUDE", -87.6298)
    timezone = timezone or os.getenv("WEATHER_TIMEZONE", "America/Chicago")

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ",".join(DEFAULT_HOURLY_VARIABLES),
        "timezone": timezone,
        "forecast_days": forecast_days,
    }

    response = requests.get(OPEN_METEO_FORECAST_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def _env_float(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None:
        return default

    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a valid float") from exc
