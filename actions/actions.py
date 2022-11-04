import requests, json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTellWeather(Action):

    def name(self) -> Text:
        return "action_tell_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city_name = next(tracker.get_latest_entity_values("place"), None)
        api_key = "0ad3ff8e75c082c6fc193348b16958b1"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" + "&lang=de"
        response = requests.get(complete_url)
        x = response.json()["main"]
        desc = response.json()["weather"]
        current_temperature = x["temp"]
        weather_description = desc[0]["description"]
        dispatcher.utter_message(f"In {city_name} sind es " + str(current_temperature) + "°C. \nAktueller Wetterstatus: " + str(weather_description))
        return []

