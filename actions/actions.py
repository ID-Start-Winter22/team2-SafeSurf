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
        dispatcher.utter_button_message("Hallo! 👋🏻, Ich bin SafeSurf 🔒. \n Gemeinsam prüfen wir deine Sicherheit im Internet. 🌐 \n Mit Check Mail example@mail.com kannst du überprüfen ob deine E-mail in einem Datenleak war \n Mit Check Passwort ExamplePasswort123 kannst du Testen ob dein Passwort sicher ist", buttons)
        return[SlotSet("CCLI", CurrentCheckListIndex)]


class nextchecklist(Action):
    def name(self) -> Text:
        return "nextchecklist"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        CurrentCheckListIndex = tracker.get_slot("CCLI")
        if CurrentCheckListIndex == "CL0":
            dispatcher.utter_message("Okay, starten wir mit Passwörtern! 🔒 \n Bei Passwörtern gibt es wichtige Dinge zu beachten:")
            dispatcher.utter_message("Deine Passwörter sollten aus Groß und Kleinbuchstaben bestehen, sowie mindestens 8-16 Zeichen lang sein. ⚡ \n Es sollten Sonderzeichen im Passwort enthalten sein. (!,?,&) 🅰️ \n Es sollten unterschiedliche Passwörter benutzt werden. \n Es sollten keine persönlichen Daten enthalten sein. Zum Beispiel Geburtstage oder Namen 🔢 \n Du kannst auch dein Passwort automatisch überprüfen lassen mit: Passwortcheck Passwort123")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Passwortcheck Hilfe 🆘", "payload": "Passwortcheck Erklärung"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL1")]
        elif CurrentCheckListIndex == "CL1":
            dispatcher.utter_message("Machen wir weiter mit 2FA 🔑")
            dispatcher.utter_message("2FA ist ein zweiter Schlüssel 🔑 zu deinem Konto. \n Dieser zweite Schlüssel ist meist ein zeit generierter 6 zahlen code und wird bei jeder erneuten Anmeldung abgefragt.")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL2")]
        elif CurrentCheckListIndex == "CL2":
            dispatcher.utter_message("Machen wir weiter mit Webseiten! 🌍 \n Du solltest nicht alle Webseite besuchen, die du findest!")
            dispatcher.utter_message("Besuche nur Webseiten mit SSL Verbindung (Grünes Schloss 🔒 neben der Link Leiste) \n Überprüfe regelmäßig deine Browsereinstellungen bezügl. Datenschutz 🌐 \n Achte bei Webseiten auf die geforderten Cookies im Cookie Banner. 🍪")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL3")]
        elif CurrentCheckListIndex == "CL3":
            dispatcher.utter_message("Machen wir weiter mit falschen/gefaketen öffentlichen Netzwerken 📶 und fake links 🔗")
            dispatcher.utter_message("Oft werden fake Links 🔗 per email versendet oder fake öffentliche Netzwerke eröffnet um Nutzerdaten zu klauen. \n Dabei sollte man auf die Korrekte schreibweise der Webseite achten.")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL4")]
        elif CurrentCheckListIndex == "CL4":
            dispatcher.utter_message("Machen wir weiter mit VPN's 📶")
            dispatcher.utter_message("Für einen zusätzlichen Schutz in öffentlichen Netzwerken kannst du einen VPN verwenden. \n Dieser Verschlüsselt deine gesendeten Informationen und schützt dich vor Attacken 🛡️.")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL5")]
        elif CurrentCheckListIndex == "CL5":
            dispatcher.utter_message("Machen wir weiter mit Datenschutzeinstellungen 🌍")
            dispatcher.utter_message("Um sich vor Tracking durch Cookies zu schützen, ist es wichtig die Datenschutzeinstellungen des Browsers Korrect einzustellen. \n Dabei ist darauf zu achten, dass die Cookies 🍪 nach schließen des Browsers gelöscht werden sollten. \n Du kannst deine Mail überprüfen lassen, ob du bei einer gehackten Datenbank von einer Webseite, bei der du dich registriert hast, dabei bist. (Siehe Mailcheck Hilfe 🆘)")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Mailcheck Hilfe 🆘", "payload": "Mailcheck Erklärung"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL6")]
        elif CurrentCheckListIndex == "CL6":
            dispatcher.utter_message("Machen wir weiter mit Antivieren Software 🛡️")
            dispatcher.utter_message("Ein Virenschutz ist eine Sicherheitsschicht 🛡️ die dein Gerät vor Schadsoftware schützt. \n Für die meisten Geräte reicht der vorinstallierte Schutz aus.")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL7")]
        elif CurrentCheckListIndex == "CL7":
            dispatcher.utter_message("Machen wir weiter mit Updates! 🔄 \n Du solltest dein System immer auf dem neusten Stand halten")
            dispatcher.utter_message("Deine Software sollte immer auf dem neusten Stand sein, dadurch werden Systemlücken geschlossen und dein System wird generell schwieriger zu knacken.")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL8")]       
        elif CurrentCheckListIndex == "CL8":
            dispatcher.utter_message("Machen wir weiter mit Online Shopping 💳")
            dispatcher.utter_message("Bei Zahlungen im Internet sollte man immer darauf achten, dass man auf vertrauenswürdigen Webseiten einkauft. \n Wichtig ist es außerdem eine sichere Zahlungsmethode zu nutzen, z.B. Paypal mit Käuferschutz 💳")
            buttons = [{"title": "Mehr Informationen 📥", "payload": "Mehr Info"}, {"title": "Abschließen 🏁", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL9")]
        elif CurrentCheckListIndex == "CL9":
            dispatcher.utter_message("JUHU! 🏁 Gemeinsam sicher im Internet. Falls du Fragen hast, oder dich mehr Informieren möchtest stelle mir einfach eine Frage oder schau dich auf unserer [Webseite](https://banifli.de/) um! 🌍")
            buttons = [{"title": "Checkliste zurücksetzen ⚒️", "payload": "ResetCL"}, {"title": "Dankeschön sagen! 💟", "payload": "Dankeschön"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL10")]          
        elif CurrentCheckListIndex == "CL10":
            dispatcher.utter_message("JUHU! 🏁 Gemeinsam sicher im Internet. Falls du Fragen hast, oder dich mehr Informieren möchtest stelle mir einfach eine Frage oder schau dich auf unserer [Webseite](https://banifli.de/) um! 🌍")
            buttons = [{"title": "Checkliste zurücksetzen ⚒️", "payload": "ResetCL"}, {"title": "Dankeschön sagen! 💟", "payload": "Dankeschön"}]
            dispatcher.utter_button_message("Möchtest du mehr Informationen, oder weitermachen?", buttons)
            return [SlotSet("CCLI", "CL10")]     
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
            dispatcher.utter_button_message("[Passwörter – Je Komplexer desto Besser](https://banifli.de/warum-es-sinnvoll-ist-komplexe-passwoerter-zu-verwenden/)", buttons)
            return [SlotSet("CCLI", "CL1")]
        elif CurrentCheckListIndex == "CL2":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[2FA - Die Erweiterung des Passworts](https://banifli.de/warum-es-sinnvoll-ist-2fa-zu-verwenden/)", buttons)
            return [SlotSet("CCLI", "CL2")]
        elif CurrentCheckListIndex == "CL3":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Verschlüsselte Webseiten](https://banifli.de/verschluesselte-webseiten/)", buttons)
            return [SlotSet("CCLI", "CL3")]
        elif CurrentCheckListIndex == "CL4":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Fake Links / Wifi Hotspots](https://banifli.de/fake-links-fake-wifi-hotspots/)", buttons)
            return [SlotSet("CCLI", "CL4")]
        elif CurrentCheckListIndex == "CL5":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[VPN – Hilfreicher Begleiter in öffentlichen Netzwerken](https://banifli.de/warum-es-sinnvoll-ist-einen-vpn-zu-verwenden-2/)", buttons)
            return [SlotSet("CCLI", "CL5")]
        elif CurrentCheckListIndex == "CL6":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Datenschutz Einstellungen im Browser](https://banifli.de/datenschutz-einstellungen-im-browser/)", buttons)
            return [SlotSet("CCLI", "CL6")]
        elif CurrentCheckListIndex == "CL7":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Vierenschutz – Warum ist dieser Wichtig?](https://banifli.de/antiviren-software/)", buttons)
            return [SlotSet("CCLI", "CL7")]
        elif CurrentCheckListIndex == "CL8":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Updates - Schließen von Systemlücken](https://banifli.de/updates-schliessen-von-systemluecken/)", buttons)
            return [SlotSet("CCLI", "CL8")]
        elif CurrentCheckListIndex == "CL9":
            dispatcher.utter_message("Mehr Infos findest du hier:")
            buttons = [{"title": "Weitermachen 🚀", "payload": "Nächster Schritt"}]
            dispatcher.utter_button_message("[Gefahren im Onlinehandel](https://banifli.de/gefahren-im-onlinehandel/)", buttons)
            return [SlotSet("CCLI", "CL9")]
        elif CurrentCheckListIndex == "CL10":
            dispatcher.utter_message("Für mehr Informationen, besuche unsere Webseite! 🌍")
            dispatcher.utter_message("[Banifli SafeSurf Blog](https://banifli.de/blog//)")
            return [SlotSet("CCLI", "CL10")]
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
        if antwort == "Mailcheck Erklärung":
            dispatcher.utter_message("Du kannst überprüfen, ob deine Accounts in einem Datenleak (Gehackte Datenbank) vorkommen. Dies kannst du mit 'Mailcheck mail@mail.com'!")
        else:
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


class pwchecker(Action):
    def name(self) -> Text:
        return "pwchecker"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        pwue = tracker.latest_message.get('text')
        if pwue == "Passwortcheck Erklärung":
            dispatcher.utter_message("Um einen Passwort Check durchzuführen, schreibe das Passwort welches du Checken willst nach 'Passwortcheck' z.B  'Passwortcheck Passwort123'")
        else:
            nlulist = ["Passwortcheck ", "PasswortCheck ", "pwcheck ", "Passwort ", "Passwort überprüfen ", "Passwortcheck Erklärung"] # COPY DATA FROM NLU
            for a in nlulist:
                if a in pwue:
                    password = pwue.replace(a, "")

            length_error = len(password) < 8
            digit_error = re.search(r"\d", password) is None
            uppercase_error = re.search(r"[A-Z]", password) is None
            lowercase_error = re.search(r"[a-z]", password) is None
            symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
            password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
            if password_ok == True:
                dispatcher.utter_message("Passwort ist okay!")
            else:
                dispatcher.utter_message("Dein Passwort ist nicht sicher. (+) = gut / (-) = schlecht")
                if length_error == True:
                    dispatcher.utter_message("Dein Passwort ist zu kurz (-)")
                if length_error == False:
                    dispatcher.utter_message("Dein Passwort ist zu lang genug! (+)")
                if digit_error == True:
                    dispatcher.utter_message("Dein Passwort enthält keine Zahlen (-)")
                if digit_error == False:
                    dispatcher.utter_message("Dein Passwort enthält Zahlen! (+)")
                if uppercase_error == True:
                    dispatcher.utter_message("Dein Passwort enthält keine Großbuchstaben (-)")
                if uppercase_error == False:
                    dispatcher.utter_message("Dein Passwort enthält Großbuchstaben (+)")
                if lowercase_error == True:
                    dispatcher.utter_message("Dein Passwort enthält keine Kleinbuchstaben (-)")
                if lowercase_error == False:
                    dispatcher.utter_message("Dein Passwort enthält Kleinbuchstaben (+)")
                if symbol_error == True:
                    dispatcher.utter_message("Dein Passwort hat keine Sonderzeichen. (-)")
                if symbol_error == False:
                    dispatcher.utter_message("Dein Passwort hat Sonderzeichen. (+)")
