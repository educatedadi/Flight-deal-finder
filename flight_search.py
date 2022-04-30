import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv("setup.env")

API_KEY = os.getenv('tequila_api_key')
tequila_endpoint = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.auth = {"apikey": API_KEY}


    def get_iata_code(self, city_name: str):
        query = {
            'term': city_name,
            'location_types': 'city',
        }
        response = requests.get(url=f'{tequila_endpoint}/locations/query', params=query, headers=self.auth)
        data = response.json()['locations']

        return data[0]['code']

    def get_prices(self, from_city_code, to_city_code, from_date, to_date):

        query = {
            'fly_from': from_city_code,
            'fly_to': to_city_code,
            'date_from': from_date,
            'date_to': to_date,
            'curr': 'GBP',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'max_stopovers': 0,
            'one_for_city': 1,
        }
        # print(query)
        response = requests.get(f'{tequila_endpoint}/v2/search', params=query, headers=self.auth)
        # print(response.json())

        try:
            result = response.json()['data'][0]
        except IndexError:
            query['max_stopovers'] = 3
            response = requests.get(f'{tequila_endpoint}/v2/search', params=query, headers=self.auth)
            print('No direct flights, looking for flights w/ stopovers')
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=len(data['route'])/2,
                via_city=data["route"][0]["cityTo"],
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        else:
            flight_data = FlightData(
                price=result["price"],
                origin_city=result["route"][0]["cityFrom"],
                origin_airport=result["route"][0]["flyFrom"],
                destination_city=result["route"][0]["cityTo"],
                destination_airport=result["route"][0]["flyTo"],
                out_date=result["route"][0]["local_departure"].split("T")[0],
                return_date=result["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data

