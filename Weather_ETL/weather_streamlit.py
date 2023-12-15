import streamlit as st
import folium
from streamlit_folium import st_folium

def fetch_data():
    conn = st.connection("postgresql", type="sql")
    df = conn.query('SELECT * FROM weather;', ttl="10m")
    return df

APP_TITLE = 'India Weather Forecast'
st.set_page_config(APP_TITLE)
st.title(APP_TITLE)
st.caption('Last Updated - 15th Dec 2023 10:30 PM')

weather_df = fetch_data()

COUNTRY_CENTRE = [20.5,78.5]
HTML_TOOLTIP = """
<style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }}
        .container {{
            width: 80%;
            margin: 10px auto;
        }}
        .info-box {{
            padding: 10px;
            background-color: #ffffff;
            border: 1px solid #cccccc;
        }}
</style>
<div class="container">
    <div class=""info-box">
            <h4>{name}</h4>
            <p>{temperature}&deg;C . {condition}</p>
        </div>
    </div>
</div>
"""
map = folium.Map(location=COUNTRY_CENTRE, zoom_start=4, scrollWheelZoom=False, tiles="CartoDB positron")

for index, row in weather_df.iterrows():
    location = int(row['lat']), int(row['long'])
    html_tooltip = HTML_TOOLTIP.format(name=row['name'], temperature=round(row['temp_c']), condition=row['condition'])
    folium.Marker(location, tooltip=html_tooltip).add_to(map)

st_map = st_folium(map, width=700, height=450)