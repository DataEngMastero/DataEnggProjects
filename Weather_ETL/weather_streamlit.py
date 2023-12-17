import streamlit as st
import folium
from datetime import datetime
from streamlit_folium import st_folium

def fetch_data(query):
    conn = st.connection("postgresql", type="sql")
    df = conn.query(query, ttl="10m")
    return df

def formatted_string(input_string):
    datetime_object = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S")
    formatted_string = datetime_object.strftime("%A, %B %d, %Y %I:%M %p")
    return formatted_string

APP_TITLE = 'India Weather Forecast'
COUNTRY_CENTRE = [20.5,78.5]
HTML_TOOLTIP = """
<style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }}
        .container {{
            width: 100%;
            margin: 0px auto;
            display: flex;
        }}
        .info-box {{
            padding: 10px;
            background-color: #ffffff;
        }}
        .image-box {{
            flex: 1;
            padding: 10px;
            background-color: #ffffff;
            text-align: center;
        }}
</style>
<div class="container">
    <div class="image-box">
        <img src="{image_url}" alt="Weather Condition Image">
    </div>
    <div class=""info-box">
            <h4>{name}</h4>
            <p>{temperature}&deg;C . {condition}</p>
        </div>
    </div>
</div>
"""




st.set_page_config(APP_TITLE)
st.title(APP_TITLE)

last_updated_query = "SELECT to_char(TO_TIMESTAMP(MAX(last_updated_epoch)),'YYYY-MM-DD HH24:MI:SS') AS last_updated_ts FROM weather;"
last_updated_ts = fetch_data(last_updated_query)
st.caption(f"Last Updated on {formatted_string(last_updated_ts['last_updated_ts'][0])}")

latest_record_query = f"""
WITH Weather_Rank AS (
    SELECT
		w.*,
        RANK() OVER (PARTITION BY name ORDER BY last_updated_epoch DESC) AS rnk
    FROM weather w
)

SELECT name, lat, long, temp_c, temp_f, condition, condition_icon, humidity, cloud
FROM Weather_Rank WHERE rnk = 1;
"""
weather_df = fetch_data(latest_record_query)

map = folium.Map(location=COUNTRY_CENTRE, zoom_start=4, scrollWheelZoom=False, tiles="CartoDB positron")
for index, row in weather_df.iterrows():
    location = int(row['lat']), int(row['long'])
    html_tooltip = HTML_TOOLTIP.format(name=row['name'], temperature=round(row['temp_c']), \
        condition=row['condition'], image_url='https:' + row['condition_icon'])
    folium.Marker(location, tooltip=html_tooltip).add_to(map)

st_map = st_folium(map, width=700, height=450)

presented_table = weather_df[['name', 'lat', 'long', 'temp_c', 'temp_f', 'condition']]
st.dataframe(
    presented_table,
    column_config={
        "name": "City",
        "lat" : "Latitude",
        "long": "Longitude",
        "temp_c": st.column_config.NumberColumn(
            "Temperature in Celsius",
            format="%.0f°C",
        ),
        "temp_f": st.column_config.NumberColumn(
            "Temperature in Fahrenheit",
            format="%.0f°F",
        ),
        "condition" : "Conditions"
    },
    hide_index=True,
)
