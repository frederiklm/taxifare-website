import streamlit as st
import datetime
import requests
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

pickup_longitude = st.text_input('Choose a pickup longitude', "93.122316")
pickup_latitude = st.text_input('Choose a pickup latitude', "93.122316")

dropoff_longitude = st.text_input('Choose a dropoff longitude', "93.122316")
dropoff_latitude = st.text_input('Choose a dropoff latitude', "93.122316")

passenger_count = st.number_input('Choose number of passengers', 1, 8, 3)
#pickup_datetime = datetime.combine(date ,time)



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



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




#f"Your predicted fare is: ${round(call_result['fare'], 2)}!"
