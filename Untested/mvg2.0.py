#########################################################
#                                                       #
# Query public transportation info from MVG.            #
#                                                       #
#                                                       #
# Author: Michael Eggers, michael.eggers@hm.edu         #
#########################################################


import requests
import json
import datetime

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
    arrival_time = None
    departure_time = None
    for connection in as_dict["connectionList"]:
        departure_time = connection["departure"]
        arrival_time   = connection["arrival"] 
        arrival = datetime.datetime.utcfromtimestamp((arrival_time + 3600000 ) / 1000).strftime('%H:%M')
        departure = datetime.datetime.utcfromtimestamp((departure_time + 3600000) / 1000).strftime('%H:%M')
        delta_time_ms = arrival_time - departure_time
        travel_time  = (delta_time_ms / 1000.0) / 60.0
        break

    return travel_time, departure, arrival

def handle_route(start, destination):
    from_station  = name_to_station(start)
    to_station    = name_to_station(destination)

    if from_station and to_station:
        print("Checking route from " + from_station["name"], from_station["id"] + " to " + to_station["name"], to_station["id"])
    else:
        return "At least one unknown station!"
    
    travel_time = get_travel_time_for_stationIDs(from_station["id"], to_station["id"])
    if travel_time:
        print("Time needed:", round(travel_time[0]), "min", "\n" "Abfahrt:", travel_time[1], "\n" "Ankunft:", travel_time[2], travel_time[3])
    else:
        return "Could not calculate travel-time for this pair of stations!"

start = input("Start ")
ende = input("Endstation ")
# Test
handle_route(start, ende)
