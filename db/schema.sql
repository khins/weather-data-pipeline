CREATE TABLE IF NOT EXISTS hourly_weather (
    forecast_time TEXT PRIMARY KEY,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    timezone TEXT NOT NULL,
    temperature_2m REAL,
    relative_humidity_2m REAL,
    precipitation REAL,
    wind_speed_10m REAL,
    loaded_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
