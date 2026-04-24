from __future__ import annotations

from typing import Any


def transform_weather(raw_weather: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten Open-Meteo hourly forecast arrays into row dictionaries."""
    hourly = raw_weather.get("hourly", {})
    times = hourly.get("time", [])

    rows: list[dict[str, Any]] = []
    for index, forecast_time in enumerate(times):
        rows.append(
            {
                "forecast_time": forecast_time,
                "latitude": raw_weather.get("latitude"),
                "longitude": raw_weather.get("longitude"),
                "timezone": raw_weather.get("timezone"),
                "temperature_2m": _value_at(hourly, "temperature_2m", index),
                "relative_humidity_2m": _value_at(hourly, "relative_humidity_2m", index),
                "precipitation": _value_at(hourly, "precipitation", index),
                "wind_speed_10m": _value_at(hourly, "wind_speed_10m", index),
            }
        )

    return rows


def _value_at(hourly: dict[str, list[Any]], field: str, index: int) -> Any:
    values = hourly.get(field, [])
    if index >= len(values):
        return None
    return values[index]
