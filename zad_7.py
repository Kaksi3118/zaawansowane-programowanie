# python3 -m pip install requests

import requests

brewery_data = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20").json()

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str or None, address_2: str or None, address_3: str or None, city: str, state_province: str, postal_code: str, country: str, longitude: float or None, latitude: float or None, phone: str or None, website_url: str or None):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return f"Brewery: {self.name}, Location: {self.city}, Type: {self.brewery_type}"
    
brewery_data = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20").json()    
print(brewery_data)

for brewery in brewery_data:
    print(Brewery(brewery['id'], brewery['name'], brewery['brewery_type'], brewery['address_1'], brewery['address_2'], brewery['address_3'], brewery['city'], brewery['state_province'], brewery['postal_code'], brewery['country'], brewery['longitude'], brewery['latitude'], brewery['phone'], brewery['website_url']))   