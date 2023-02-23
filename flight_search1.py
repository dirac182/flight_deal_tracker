from dotenv import load_dotenv
import os
from manage_data import DatManage
from flight_data import FlightData
import requests

load_dotenv("C:/Env Variables/.env")
TEQ_API_KEY = os.getenv("tequila_api_key")
class FlightSearch():

    def __init__(self):
        super().__init__()
        self.dm = DatManage()
        self.fd = FlightData()
        self.teq_endpoint = "https://api.tequila.kiwi.com/"
        self.teq_header = {
            "apikey": TEQ_API_KEY
        }
        self.teq_parameters = {
            "fly_from": "CHI"
        }
    def get_iata(self):
        self.query_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.cities = self.dm.get_data()
        self.header = {
                "apikey": TEQ_API_KEY,
                "Content-Type": "application/json"
        }
        for idx,city in enumerate(self.cities):
            parameter = {
                "term": f"{city}",
                "location_type": "city",
                "locale": "en-US",
            }
            response = requests.get(url=self.query_endpoint,headers=self.header,params=parameter)
            try:
                iata = response.json()["locations"][0]["code"]
                #self.dm.update_iata(idx+2,iata)
                self.fd.flight_prices(idx+2, city)
            except IndexError:
                self.dm.update_iata(idx+2,"error")



fs = FlightSearch()
fs.get_iata()
