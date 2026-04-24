from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


DATABASE_PATH = Path("weather.db")
SCHEMA_PATH = Path("db/schema.sql")


def initialize_database(
    database_path: Path = DATABASE_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> None:
    """Create local SQLite tables if they do not exist."""
    with sqlite3.connect(database_path) as connection:
        connection.executescript(schema_path.read_text(encoding="utf-8"))


def insert_weather_rows(
    rows: list[dict[str, Any]],
    database_path: Path = DATABASE_PATH,
) -> int:
    if not rows:
        return 0

    with sqlite3.connect(database_path) as connection:
        connection.executemany(
            """
            INSERT OR REPLACE INTO hourly_weather (
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
                :forecast_time,
                :latitude,
                :longitude,
                :timezone,
                :temperature_2m,
                :relative_humidity_2m,
                :precipitation,
                :wind_speed_10m
            )
            """,
            rows,
        )
        return len(rows)
