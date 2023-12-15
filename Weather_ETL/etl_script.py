import requests
import config
import pandas as pd
from postgres import PostgresClient

url = "https://weatherapi-com.p.rapidapi.com/current.json"
headers = {
	"X-RapidAPI-Key": config.RAPID_API_KEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
cities = config.CITIES

# Weather API Calls
def get_weather_dataset():
    weather_df = pd.DataFrame()
    for city in cities:
        print(f"Fetching Results for City - {city['name']} :: ")
        querystring = {"q": city['lat_long']}
        
        response = requests.get(url, headers=headers, params=querystring)
        flat_response = pd.json_normalize(response.json())
        print(response.json())

        city_df = flat_response[['location.name', 'location.region', 'location.country', 'location.lat', 'location.lon', 'location.tz_id', 'current.temp_c', 'current.temp_f', 'current.condition.text', 'current.condition.icon', 'current.wind_kph', 'current.pressure_in', 'current.precip_in', 'current.humidity', 'current.cloud', 'current.last_updated_epoch']]
        weather_df = pd.concat([weather_df, city_df], ignore_index=True)

    print(len(weather_df))
    weather_df.to_csv('Weather_DF.csv', index=False)
get_weather_dataset()

# Load Dataset in Postgres DB
postgres_client = PostgresClient(config.HOST, config.DBNAME, config.USERNAME, config.PASSWORD)
print(config.weather_create_query)
postgres_client.execute_query(config.weather_create_query)

temp_df = pd.read_csv('Weather_DF.csv')
for idx, row in temp_df.iterrows(): 
    postgres_client.execute_query(config.weather_insert_query, list(row))

postgres_client.connection_close()