import pip._vendor.requests, json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_tell_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Wie ist das Wetter?")

         return []

api_key = "0ad3ff8e75c082c6fc193348b16958b1"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" + "&lang=de"
response = pip._vendor.requests.get(complete_url)
x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(
        "\n " +
        "Temperature = " +
                    str(current_temperature) + "°C" +
        "\n " +
        "\n Luftdruck = " +
                    str(current_pressure) + " hPa" +
                "\n " +
        "\n Humidity = " +
                    str(current_humidity) + "%" +
                "\n " +
        "\n Beschreibung = " +
                    str(weather_description) +
        "\n " +
        "\n Have a Nice Day!!!! " +
        "\n " )

else:
    print(" City Not Found ")