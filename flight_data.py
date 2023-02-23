import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from manage_data import DatManage
import datetime as dt
import os

load_dotenv("C:/Env Variables/.env")

class FlightData(DatManage):

    def __init__(self):
        super().__init__()
        self.dm = DatManage()
        self.TEQ_API_KEY = os.getenv("tequila_api_key")
        self.teq_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.today = dt.datetime.today()
        self.todays_date = self.today.strftime("%d/%m/%Y")
        self.six_months = (dt.datetime.now() + dt.timedelta(days=30*6)).strftime("%d/%m/%Y")
        self.teq_header = {
            "apikey": self.TEQ_API_KEY
            }

    def flight_prices(self,idx,city):
        teq_parameters = {
            "fly_from": "CHI",
            "fly_to": f"{city}",
            "date_from": f"{self.todays_date}",
            "date_to": f"{self.six_months}",
            "adults": 2,
            "curr": "USD",
            "locale": "en"
        }
        results = requests.get(url=self.teq_endpoint,params=teq_parameters,headers=self.teq_header)
        data = results.json()["data"]
        lowest_price = 1000000
        for prices in data:
            price = prices["price"]
            if price < lowest_price:
                lowest_price = price
        self.dm.update_prices(idx, lowest_price, city)

