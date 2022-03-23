from geopy.geocoders import Nominatim
import spacy
  
nlp = spacy.load('en_core_web_sm')


def address_to_coordinates(address):
    # Geopy has different Geocoding services that you can choose from, including Google Maps, ArcGIS, AzureMaps, Bing, etc. Some of them require API keys, while others do not need.
    # Complete list of encoder: https://geopy.readthedocs.io/en/latest/#module-geopy.geocoders
    # Nominatim Geocoding service, which is built on top of OpenStreetMap data
    
    geolocator = Nominatim(user_agent="daisi_geocoder")

    location = geolocator.geocode(address)

    data = {
        "address": location.address if location else None,
        "lat": location.latitude if location else None,
        "lon": location.longitude if location else None,
    }

    return data

def get_locations(texts):
    locations = []
    for text in texts:
        doc = nlp(text)
        
        for ent in doc.ents:
            if ent.label_ in ["GPE"]:
                coordinates = address_to_coordinates(ent.text)
                if coordinates["lat"]:
                    locations.append(coordinates)
    
    return {"result": locations}