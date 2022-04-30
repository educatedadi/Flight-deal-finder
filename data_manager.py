import requests
from dotenv import load_dotenv
import os

load_dotenv("setup.env")
bearer_code = os.getenv('sheety_bearer_code')
auth = {"Authorization": f"Bearer {bearer_code}"}

class DataManager:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/2a43d705366946a9bc92969ac393e869/flightDealsProject/prices"

    def get_data(self):
        sheety_response = requests.get(self.sheety_endpoint, headers=auth)
        self.sheety_data = sheety_response.json()
        return self.sheety_data['prices']

    def put_iata_code(self, id, code):
        iata_param = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(self.sheety_endpoint + f'{id}', json=iata_param, headers=auth)
