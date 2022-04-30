# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta

FROM_CITY_IATA = 'LON'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()
iata_code = []

# Checks if all the cities have IATA code present, if not then look for it and put it in
for count in range(len(sheet_data)):
    if not sheet_data[count]['iataCode']:
        num = flight_search.get_iata_code(sheet_data[count]['city'])
        iata_code.append(num)
        data_manager.put_iata_code(id=sheet_data[count]['id'], code=num)
        sheet_data[count]["iataCode"] = iata_code[count]


tomorrow_date = datetime.today() + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%d/%m/%Y")
six_month_date = datetime.today() + timedelta(days=(30 * 6))
six_month_date = six_month_date.strftime("%d/%m/%Y")

# Search for the flight form base city to all cities and gives the lowest price
for item in sheet_data:
    # print(item['iataCode'])
    flight_data_item = flight_search.get_prices(
        from_city_code=FROM_CITY_IATA,
        to_city_code=item['iataCode'],
        from_date=tomorrow_date,
        to_date=six_month_date,
    )
    # if found a price lower than average price then sends a notification
    if flight_data_item is None:
        continue

    if flight_data_item.price <= item['lowestPrice']:
        message = f'Low price alert! Only ${flight_data_item.price} to fly from ' \
                  f'{flight_data_item.origin_city}-{flight_data_item.origin_airport} to ' \
                  f'{flight_data_item.destination_city}-{flight_data_item.destination_airport}, from ' \
                  f'{flight_data_item.out_date} to {flight_data_item.return_date} ' \
                  f'\nGo book it right now from here: {flight_data_item.book_link}'

        if flight_data_item.stop_overs > 0:
            message += f"\nFlight has {flight_data_item.stop_overs} stop over, via {flight_data_item.via_city}."
            print(message)

        # notification_manager.send_alert(message=message)

        # notification_manager.send_emails(message)

print('Done✔')
