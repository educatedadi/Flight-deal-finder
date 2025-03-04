import requests
from twilio.rest import Client
from flight_data import FlightData
from dotenv import load_dotenv
import os
import smtplib

load_dotenv("setup.env")

email = os.getenv('by_email')
password = os.getenv('e_mail_pass')
mobilenum = os.getenv('mobile_num')

bearer_code = os.getenv('sheety_bearer_code')
auth = {"Authorization": f"Bearer {bearer_code}"}
sheety_user_endpoint = 'https://api.sheety.co/2a43d705366946a9bc92969ac393e869/flightDealsProject/users'

account_sid = os.getenv('twilio_account_sid')
auth_token = os.getenv('twilio_auth_token')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_alert(self, message: str):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid='MGd063b86b7d5c691a9261816e01245c06',
            body=message,
            to=mobilenum
        )
        print('Message sent!')

    def send_emails(self, message):
        response = requests.get(url=sheety_user_endpoint, headers=auth)
        users_data = response.json()['users']

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)

            for user in users_data:
                f_name = user['firstName']
                l_name = user['lastName']
                e_mail = user['email']

                connection.sendmail(
                    from_addr=email,
                    to_addrs=f'{e_mail}',
                    msg=f'Subject:Low Price Alert!\n\nHello {f_name}, We have found a deal for you! \n{message}'
                )


        print('Mails sent!')
