import requests, json, random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class MainMenu(Action):
    def name(self) -> Text:
        return "action_home_menu"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        buttons = [{"title": "Checkliste durchführen 📝", "payload": "Checkliste"}, {"title": "Zurück zum Hauptmenü 🏠", "payload": "Hallo"}]
        dispatcher.utter_button_message("Hallo! 👋🏻, Ich bin SafeSurf 🔒. \n Gemeinsam prüfen wir deine Sicherheit im Internet. 🌐", buttons)
        return[]


class CheckAccount(Action):
    def name(self) -> Text:
        return "action_check_account"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        antwort = tracker.latest_message.get('text')
        dispatcher.utter_message(f"Deine Mailadresse ist: {antwort}")
        return[]




"""
class ActionTellWeather(Action):

    def name(self) -> Text:
        return "action_tell_weather"
     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city_name = next(tracker.get_latest_entity_values("place"), None)
        api_key = "XYZ"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" + "&lang=de"
        response = requests.get(complete_url)
        x = response.json()["main"]
        desc = response.json()["weather"]
        current_temperature = x["temp"]
        weather_description = desc[0]["description"]
        dispatcher.utter_message(f"In {city_name} sind es " + str(current_temperature) + "°C. \nAktueller Wetterstatus: " + str(weather_description))
        return []

class Jokes(Action):
    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://witzapi.de/api/joke"
        response = requests.get(url)
        jr = response.json()[0]
        joke = jr["text"]
        dispatcher.utter_message("Okay, hier ist ein Witz für dich. \n" + joke)
        return []

class quote(Action):
    def name(self) -> Text:
        return "action_tell_quote"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:  
        url = "https://type.fit/api/quotes/"
        response = requests.get(url)
        qod = response.json()[0:]
        output = random.choice(qod)
        dispatcher.utter_message("Okay, hier ist ein Spruch für dich.\n" + output["text"] + " Author: " + output["author"])
        return[]
 """