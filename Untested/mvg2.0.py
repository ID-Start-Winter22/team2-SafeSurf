#########################################################
#                                                       #
# Query public transportation info from MVG.            #
#                                                       #
#                                                       #
# Author: Michael Eggers, michael.eggers@hm.edu         #
#########################################################


import requests
import json

MVG_STATION_URL = "https://www.mvg.de/api/fahrinfo/location/queryWeb"
MVG_ROUTING_URL = "https://www.mvg.de/api/fahrinfo/routing"

def name_to_station(name: str):
    mvg_resp = requests.get(MVG_STATION_URL, params={"q": name})
    
    if mvg_resp.status_code != requests.codes.ok:
        return None
    
    as_dict = mvg_resp.json()

    station = None
    for location in as_dict["locations"]:
        if location["type"] == "station":
            station = { "id": location["id"], "name": location["name"] }
            break

    return station

# Returns travel time in minutes
def get_travel_time_for_stationIDs(station_a, station_b):
    mvg_resp = requests.get(MVG_ROUTING_URL, params={ "fromStation": station_a, "toStation": station_b })

    if mvg_resp.status_code != requests.codes.ok:
        return None

    as_dict = mvg_resp.json()

    travel_time = None
    for connection in as_dict["connectionList"]:
        departure_time = connection["departure"]
        arrival_time   = connection["arrival"]
        delta_time_ms = arrival_time - departure_time
        travel_time   = (delta_time_ms / 1000.0) / 60.0
        break

    return travel_time

# def get_train_type(station_a, station_b):
#     mvg_resp = requests.get(MVG_ROUTING_URL, params={ "Station": station_a, "Sation": station_b})

#     if mvg_resp.satus_code != requests.codes.ok:
#         return None

#     as_dict = mvg_resp.json()

#     train_type = None
#     for departures in as_dict["connectionList"]:


def handle_route(start, destination):
    from_station  = name_to_station(start)
    to_station    = name_to_station(destination)
    mvg_resp = requests.get(MVG_ROUTING_URL, params={ "fromStation": start, "toStation": destination})

    if mvg_resp.status_code != requests.codes.ok:
        return "error"

    as_dict = mvg_resp.json()

    if from_station and to_station:
        print("Route von " + from_station["name"]+ " zu " + to_station["name"]+ " wird geprüft")
    else:
        return "At least one unknown station!"

    for connection in as_dict["connectionList"]:
        departure_time = connection["departure"]
        arrival_time   = connection["arrival"]
        return "test"

    travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
    if travel_time:
        print("Time needed:", travel_time, "min", "Abfahrt", departure_time)
    else:
        return "Could not calculate travel-time for this pair of stations!"

# Test
print(handle_route("Holzapfelkreuth", "Poccistr"))




# Bisher nicht am Laufen aber ich bekomme wenigstens ein paar output
