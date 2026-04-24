from ingestion.fetch_weather import fetch_weather
from transformation.transform_weather import transform_weather
from utils.db import initialize_database, insert_weather_rows


def main() -> None:
    initialize_database()
    raw_weather = fetch_weather()
    rows = transform_weather(raw_weather)
    inserted_count = insert_weather_rows(rows)
    print(f"Loaded {inserted_count} hourly weather rows.")


if __name__ == "__main__":
    main()
