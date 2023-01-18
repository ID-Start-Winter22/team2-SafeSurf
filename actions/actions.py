import requests, json, random
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import re
load_dotenv()
hibp_api_key = os.getenv("hibp_api_key")


class MainMenu(Action):
    def name(self) -> Text:
        return "action_home_menu"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        CurrentCheckListIndex = "CL0"
        buttons = [{"title": "Checkliste durchführen 📝", "payload": "Checkliste starten"}, {"title": "Zurück zum Hauptmenü 🏠", "payload": "Hallo"}]
        dispatcher.utter_button_message("Hallo! 👋🏻, Ich bin SafeSurf 🔒. \n Gemeinsam prüfen wir deine Sicherheit im Internet. 🌐", buttons)
        return[SlotSet("CCLI", CurrentCheckListIndex)]


class nextchecklist(Action):
    def name(self) -> Text:
        return "nextchecklist"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        CurrentCheckListIndex = tracker.get_slot("CCLI")
        if CurrentCheckListIndex == "CL0":
            dispatcher.utter_message("Okay, starten wir mit Passwörtern! 🔒 \nBei Passwortern gibt es wichtige Dinge zu beachten:")
            dispatcher.utter_message("Deine Passwörter sollten aus Groß und Kleinbuchstaben bestehen, sowie mindestens 8-16 Zeichen lang sein. ⚡ \n Es sollten Sonderzeichen im Passwort enthalten sein. (!,?,&) 🅰️ \n Es sollten unterschiedliche Passwörter benutzt werden. \n Es sollten keine persönlichen Daten enthalten sein. Zum Beispiel Geburtstage oder Namen 🔢 \n Du kannst auch dein Passwort automatisch überprüfen lassen mit: Passwortcheck Passwort123")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL1")]
        elif CurrentCheckListIndex == "CL1":
            dispatcher.utter_message(CurrentCheckListIndex)
            dispatcher.utter_message("Machen wir Weiter mit Webseiten! 🌍 \n Du solltest nicht Webseite besuchen, die du findest!")
            dispatcher.utter_message("Besuche nur Webseiten mit SSL Verbindung (Grünes Schloss 🔒 neben der Link Leiste) \n Überprüfe regelmäßig deine Browsereinstellungen bezügl. Datenschutz 🌐 \n Achte bei Webseiten auf die geforderten Cookies im Cookie Banner. 🍪")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL2")]
        elif CurrentCheckListIndex == "CL2":
            dispatcher.utter_message(CurrentCheckListIndex)
            dispatcher.utter_message("Machen wir Weiter mit Webseiten! 🌍 \n Du solltest nicht Webseite besuchen, die du findest!")
            dispatcher.utter_message("Besuche nur Webseiten mit SSL Verbindung (Grünes Schloss 🔒 neben der Link Leiste) \n Überprüfe regelmäßig deine Browsereinstellungen bezügl. Datenschutz 🌐 \n Achte bei Webseiten auf die geforderten Cookies im Cookie Banner. 🍪")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL3")]
        elif CurrentCheckListIndex == "CL4":
            dispatcher.utter_message("Machen wir Weiter mit Webseiten! 🌍 \n Du solltest nicht Webseite besuchen, die du findest!")
            dispatcher.utter_message("Besuche nur Webseiten mit SSL Verbindung (Grünes Schloss 🔒 neben der Link Leiste) \n Überprüfe regelmäßig deine Browsereinstellungen bezügl. Datenschutz 🌐 \n Achte bei Webseiten auf die geforderten Cookies im Cookie Banner. 🍪")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL4")]
        else:
            dispatcher.utter_message(f"Oh oh! Fehler: CCLI: {CurrentCheckListIndex}")
        return []


class mehrinfo(Action):
    def name(self) -> Text:
        return "mehr_info"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        CurrentCheckListIndex = tracker.get_slot("CCLI")
        if CurrentCheckListIndex == "CL1":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL1")]
        elif CurrentCheckListIndex == "CL2":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL2")]
        elif CurrentCheckListIndex == "CL3":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL3")]
        elif CurrentCheckListIndex == "CL4":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL4")]
        elif CurrentCheckListIndex == "CL5":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL5")]
        elif CurrentCheckListIndex == "CL6":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL6")]
        elif CurrentCheckListIndex == "CL7":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL7")]
        elif CurrentCheckListIndex == "CL8":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL8")]
        elif CurrentCheckListIndex == "CL9":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL9")]
        elif CurrentCheckListIndex == "CL10":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL10")]
        elif CurrentCheckListIndex == "CL11":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL11")]
        elif CurrentCheckListIndex == "CL12":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL12")]
        elif CurrentCheckListIndex == "CL13":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL13")]
        elif CurrentCheckListIndex == "CL14":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL14")]
        elif CurrentCheckListIndex == "CL15":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL15")]
        elif CurrentCheckListIndex == "CL16":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL16")]
        elif CurrentCheckListIndex == "CL17":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL17")]
        elif CurrentCheckListIndex == "CL18":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL18")]
        elif CurrentCheckListIndex == "CL19":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL19")]
        elif CurrentCheckListIndex == "CL20":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL20")]
        elif CurrentCheckListIndex == "CL21":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL21")]
        elif CurrentCheckListIndex == "CL22":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            dispatcher.utter_message("https://banifli.de/verschluesselte-webseiten/")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/", buttons)
            return [SlotSet("CCLI", "CL22")]
        else:
            dispatcher.utter_message(f"Oh oh! Fehler: CCLI: {CurrentCheckListIndex}. \n Bitte Starte die Checkliste neu mit der Nachricht: ResetCL")
        return []


class resetchecklist(Action):
    def name(self) -> Text:
        return "resetchecklist"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        CurrentCheckListIndex = "CL0"
        dispatcher.utter_message("Ich habe deinen Fortschritt der Liste gelöscht. Starte nun erneut über das Hauptmenü.")
        return [SlotSet("CCLI", CurrentCheckListIndex)]



class CheckAccount(Action):
    def name(self) -> Text:
        return "action_check_account"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        antwort = tracker.latest_message.get('text')
        extract_email_pattern = r"\S+@\S+\.\S+"
        valid_email_pattern = '[A-Za-z0-9]+[\.\-\_A-Za-z0-9]*[@]\w+[.]\w+'
        matchList = re.findall(extract_email_pattern, antwort)
        match = ''.join(matchList)
        validList = re.findall(valid_email_pattern,match)
        valid = ''.join(validList)
        if valid == match:   
            hibp_api_key = os.getenv("hibp_api_key")
            url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + match
            payload={}
            headers = {
              'hibp-api-key': str(hibp_api_key),
              'format': 'application/json',
              'timeout': '2.5',
              'HIBP': str(hibp_api_key),
            }
            
            response = requests.request("GET", url, headers=headers, data=payload)
            
            string = response.text
            # use regular expressions to match and replace only the "Name": part of the object keys
            string = re.sub('"Name":', '', string)
            string = string.replace('[', '')
            string = string.replace(']', '')
            string = string.replace('{', '')
            string = string.replace('}', '')
            if len(string) < 2:
                dispatcher.utter_message("Sieht gut aus! Dein Account ist in keiner bekannten Datenliste vorhanden!")
            elif len(string) > 2:
                dispatcher.utter_message(f"Oh nein! Du solltest deine Passwort, die du auf diesen Seiten/Apps benutzt ändern: " + string)
        else:
            dispatcher.utter_message("Sieht gut aus! Dein Account ist in keiner bekannten Datenliste vorhanden!")

        return[]


class CheckAccount(Action):
    def name(self) -> Text:
        return "action_check_account"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:

        pwue = tracker.get_intent_of_latest_message('text')
        nlulist = ["Passwortcheck ", "PasswortCheck ", "pwcheck ", "Passwort ", "Passwort überprüfen "] # COPY DATA FROM NLU
        for a in nlulist:
            if a in pwue:
                password =  pwue.replace(a, "")
        length_error = len(password) < 8
        digit_error = re.search(r"\d", password) is None
        uppercase_error = re.search(r"[A-Z]", password) is None
        lowercase_error = re.search(r"[a-z]", password) is None
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
        password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

        if password_ok == True:
            dispatcher.utter_message("Passwort ist okay")
        else:
            dispatcher.utter_message("Dein Passwort ist nicht sicher.")
            if length_error == True:
                dispatcher.utter_message("Dein Passwort ist zu kurz")
            if digit_error == True:
                dispatcher.utter_message("Dein Passwort enthält keine Zahlen")
            if uppercase_error == True:
                dispatcher.utter_message("Dein Passwort enthält keine Großbuchstaben")
            if lowercase_error == True:
                dispatcher.utter_message("Dein Passwort enthält keine Kleinbuchstaben")
            if symbol_error == True:
                dispatcher.utter_message("Dein Passwort hat keine Sonderzeichen.")