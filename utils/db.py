from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import psycopg


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://weather_user:weather_password@localhost:5432/weather_data",
)
SCHEMA_PATH = Path("db/schema.sql")


def initialize_database(schema_path: Path = SCHEMA_PATH) -> None:
    """Create Postgres tables if they do not exist."""
    with psycopg.connect(DATABASE_URL) as connection:
        connection.execute(schema_path.read_text(encoding="utf-8"))


def insert_weather_rows(rows: list[dict[str, Any]]) -> int:
    if not rows:
        return 0

    with psycopg.connect(DATABASE_URL) as connection:
        connection.executemany(
            """
            INSERT INTO hourly_weather (
                forecast_time,
                latitude,
                longitude,
                timezone,
                temperature_2m,
                relative_humidity_2m,
                precipitation,
                wind_speed_10m
            )
            VALUES (
                %(forecast_time)s,
                %(latitude)s,
                %(longitude)s,
                %(timezone)s,
                %(temperature_2m)s,
                %(relative_humidity_2m)s,
                %(precipitation)s,
                %(wind_speed_10m)s
            )
            ON CONFLICT (forecast_time, latitude, longitude) DO UPDATE SET
                latitude = EXCLUDED.latitude,
                longitude = EXCLUDED.longitude,
                timezone = EXCLUDED.timezone,
                temperature_2m = EXCLUDED.temperature_2m,
                relative_humidity_2m = EXCLUDED.relative_humidity_2m,
                precipitation = EXCLUDED.precipitation,
                wind_speed_10m = EXCLUDED.wind_speed_10m,
                loaded_at = CURRENT_TIMESTAMP
            """,
            rows,
        )
        return len(rows)
