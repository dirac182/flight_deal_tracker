#import requests
import pandas
#from dotenv import load_dotenv
#from requests.auth import HTTPBasicAuth
import os

data = pandas.read_csv("Flight Data - Sheet1.csv")
print(data["City"])

class DatManage():

    def __init__(self):
        self.data = pandas.read_csv("Flight Data - Sheet1.csv")

    def get_cities(self):
        self.cities = self.data["City"]
        return self.cities

    def update_iata(self,idx,code):
        self.api_put_endpoint = f"https://api.sheety.co/95f4ef8f4f6b6183d8dcffd957a0383b/flightData/sheet1/{idx}"
        self.update_json = {
            "sheet1": {
                "iata": f"{code}"
            }
        }
        self.response = requests.put(url=self.api_put_endpoint,auth=self.basic,json=self.update_json)
        print(self.response.text)

    def update_prices(self,idx,lowest, city):
        request = requests.get(url=self.api_get_endpoint, auth=self.basic)
        data = request.json()["sheet1"]
        print(data)
        for row in data:
            if row["city"] == city: #and (row["lowestPrice"] > lowest or row["lowestPrice"] == 0):
                update_json = {
                    "sheet1": {
                        "lowestPrice": f"{lowest}"
                    }
                }
                response = requests.put(url=self.api_put_endpoint, auth=self.basic, json=update_json)
                print(response.text)



        # print(idx,lowest)
        # print(data)

# data = DatManage()
# data.get_data()