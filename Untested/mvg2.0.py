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

start = input("Start ")
destination = input("Destination ")

from_station = start
to_sation = destination

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
def get_travel_time_for_stationIDs(start, destination):
    mvg_resp = requests.get(MVG_STATION_URL, params={ "Station": start, "Sation": destination})

    if mvg_resp.satus_code != requests.codes.ok:
        return None
    

    as_dict = mvg_resp.json()

    travel_time = None
    train_type = None
    departure_time = None
    arrival_time = None

    for connection in as_dict["connectionList"]:
        departure_time = connection["departure"]
        arrival_time   = connection["arrival"]
        delta_time_ms = arrival_time - departure_time
        travel_time   = (delta_time_ms / 1000.0) / 60.0
        train_type = ["list"]
        break

    return train_type + arrival_time + departure_time + travel_time

def handle_route(start, destination):
    from_station  = name_to_station(start)
    to_station    = name_to_station(destination)

    if from_station and to_station:
        print("Route von " + from_station["id"] + " zu " + to_station["id"]+ " wird geprüft")
    else:
        return "At least one unknown station!"

    departure_time = get_travel_time_for_stationIDs(from_station["id"])
    if departure_time:
        print("Departure Time: ", departure_time)
    else:
        return "Could not calculate departure-time for this pair of stations!"

    arrival_time = get_travel_time_for_stationIDs(to_station["id"])
    if arrival_time:
        print("Arrival Time: ", arrival_time)
    else:
        return "Could not calculate arrival-time for this pair of stations!"

    travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
    if travel_time:
        print("Time needed:", travel_time, "min")
    else:
        return "Could not calculate travel-time for this pair of stations!"

print(handle_route(start, destination))
