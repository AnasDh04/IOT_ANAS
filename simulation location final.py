



#GOOD CODE 


import json
import random
import time
from datetime import datetime, timedelta
import requests  # Importing requests library
from bson import ObjectId  # Importing ObjectId

# Simulated server URL
server_url = "http://localhost:2000/"

# Modified function to send data to a server using requests
def send_data(data, table_name):
    full_url = f"{server_url}{table_name}"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(full_url, json=data, headers=headers, timeout=3)
        response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes
        print(f"Data sent to {table_name}. HTTP Response Code: {response.status_code}")
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")

# Function to simulate the generation of new locations leading to the warehouse
def generate_new_location(thing_id):
    new_location_id = ObjectId()  # Generate new ObjectId
    location_description = f"Checkpoint {new_location_id}"
    location_properties = {"status": "en_route"}

    location_data = {
        "id_location": str(new_location_id),  # Convert ObjectId to string
        "Name": f"Location for Thing {thing_id}",
        "Description": location_description,
        "Properties": location_properties,
        "EncodingType": "application/vnd.geo+json",
        "Location": {
            "type": "Point",
            "coordinates": [random.uniform(-180, 180), random.uniform(-90, 90)]
        }
    }
    send_data(location_data, "Location")

    return new_location_id

# Modified function to simulate location data for a Thing with ObjectId
def simulate_location_data(thing_id):
    thing_id_obj = ObjectId(thing_id)  # Convert thing_id to ObjectId
    location_id = generate_new_location(thing_id)
    id_historical=ObjectId()
    time_now = datetime.now()

    thing_location_data = {
        "id_thing": str(thing_id_obj),  # Convert ObjectId to string
        "id_location": str(location_id),  # Convert ObjectId to string
        "timestamp": time_now.isoformat()
    }
    send_data(thing_location_data, "ThingLocation")

    historical_location_data = {
        "id_historical":  str(id_historical),  # Random historical ID
        "id_thing": str(thing_id_obj),  # Convert ObjectId to string
        "Time": time_now.isoformat()
    }
    send_data(historical_location_data, "HistoricalLocation")

    history_with_location_data = {
        "id_historical": str(id_historical),
        "id_location": str(location_id)  # Convert ObjectId to string
    }
    send_data(history_with_location_data, "HistoryWithLocation")

# Function to simulate the journey of a Thing over time
def simulate_journey(thing_id, duration_in_seconds, interval_in_seconds):
    end_time = datetime.now() + timedelta(seconds=duration_in_seconds)
    while datetime.now() < end_time:
        simulate_location_data(thing_id)
        time.sleep(interval_in_seconds)

# Simulate the journey of Thing 1 for 30 seconds with an interval of 10 seconds
simulate_journey(thing_id="65afe6903a22637b465ed28e", duration_in_seconds=30, interval_in_seconds=10)
