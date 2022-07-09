# US Air Quality Monitoring Project
# By Dan and Jenny

import requests
import json
import zipcodes
import datetime


# payload = {} air_API = requests.post('https://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=02148
# &date=2022-06-21&distance=25&API_KEY=E7C77666-4F3C-4065-B861-F5CCCC069C00', data=payload)

def distance_valid(num):
    return num.isNumeric() and num < 0


def pull_data():
    print("Welcome to the Air Quality Monitoring program. If you would like to obtain weather data, please enter the "
          "following:")

    user_zip = input("What is your zip code? ")
    while not zipcodes.is_real(user_zip):
        print("Please enter a valid value for zipcode.")
        user_zip = input("What is your zip code? ")

    user_date = input("When is the date? (YYYY/MM/DD) ")
    year, month, day = user_date.split('-')
    while not datetime.date(int(year) > 2003, int(month) > 1, int(day) > 1):
        print("Please enter a valid date in the format YYYY-MM-DD.")
        user_date = input("When is the date? (YYYY-MM-DD) ")

    user_distance = input("How far are you searching for the radius to your location? (mi) ")
    while not user_distance.isdigit():
        print("Please enter a valid value for miles.")
        user_distance = input("How far are you searching for the radius to your location? (mi) ")

    link = f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={user_zip}&date={user_date}&distance={int(user_distance)}&API_KEY=2D61DE65-ECB2-4E5E-B2F0-46CB789F0C84"

    air_API = requests.get(link)
    aqi_list = []  # will be used to store the AQI values

    # converts the air_API text form into JSON, this is now a list that looks like this [{"DateIssue":...},
    # {"DateIssue":...}, ...]
    air_JSON = json.loads(air_API.text)

    # Iterate through every dict in the air_JSON list, grab the value to the key you want, we want AQI, so access it
    # directly via dict["AQI"]
    for dict in air_JSON:
        aqi_list.append(dict["AQI"])

    print(aqi_list)


pull_data()
