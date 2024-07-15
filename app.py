import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd
from streamlit_folium import st_folium
import folium
from folium.plugins import Draw


'''
# New York Taxi Fare Calculation
'''

st.markdown('''
This website will predict the estimated costs of your cab ride in New York
''')

'''
## Please Insert the Information
'''

import datetime

date = st.date_input(
    "At what day do you want to take the ride?",
    datetime.date(2019, 7, 6))
#st.write('Your birthday is:', d)

time = st.time_input('At what time do you want to take the ride? ', datetime.time(8, 45))

pickup_longitude = st.text_input('Choose a pickup longitude', "-74.0060")
pickup_latitude = st.text_input('Choose a pickup latitude', "40.7128")

dropoff_longitude = st.text_input('Choose a dropoff longitude', "-74.0060")
dropoff_latitude = st.text_input('Choose a dropoff latitude', "40.8128")

passenger_count = st.number_input('Choose number of passengers', 1, 8, 3)
#pickup_datetime = datetime.combine(date ,time)



#url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



para_dict = {"pickup_datetime":f'{date} {time}',
             "pickup_longitude": pickup_longitude,
             "pickup_latitude": pickup_latitude,
             "dropoff_longitude": dropoff_longitude,
             "dropoff_latitude": dropoff_latitude,
             "passenger_count": passenger_count
             }


url = "https://taxifare.lewagon.ai/predict"
call_result = requests.get(url, params=para_dict).json()

if st.button('Calculate fare'):
    f"Your predicted fare is: ${round(call_result['fare'], 2)}!"



#@st.cache
def get_map_data():

    return pd.DataFrame({
        "lat" : [float(pickup_latitude), float(dropoff_latitude)],
        "lon" :  [float(pickup_longitude), float(dropoff_longitude)]
    })

df = get_map_data()
st.map(df, latitude = "lat",  longitude='lon', size = 50, zoom =10)

CENTRAL_COORDS = [40.71427, -74.00597]

map = folium.Map(location = CENTRAL_COORDS, zoom_start =10)

##draw = Draw()

#draw.add_to(map)

pickup_icon = folium.Icon(color='green', icon='glyphicon glyphicon-arrow-up')
dropoff_icon = folium.Icon(color='red', icon='glyphicon glyphicon-arrow-down')

folium.Marker([float(pickup_latitude), float(pickup_longitude)], tooltip='Pickup', icon = pickup_icon).add_to(map)
folium.Marker([float(dropoff_latitude), float(dropoff_longitude)], tooltip='Dropoff', icon = dropoff_icon).add_to(map)

st_data = st_folium(map, width = 1000)

#st.map()
