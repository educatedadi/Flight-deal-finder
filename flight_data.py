import requests
import pprint


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date, stop_overs=0, via_city='',):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city

        google_endpoint = f'https://www.google.co.uk/flights?hl=en#flt={origin_airport}.' \
                          f'{destination_airport}.{out_date}*{destination_airport}.{origin_airport}.{return_date}'
        self.book_link = google_endpoint

