# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class ActionHoroscope(Action):
    def name(self):
        return "action_horoscope"

    def run(self, dispatcher, tracker, domain):
        # fetch horoscope from db
        # print message containing text for each horoscope
        return []


class ActionSuscription(Action):
    def name(self):
        return "action_suscription"

    def run(self, dispatcher, tracker, domain):

        # pass the email saved in slot to database
        return []
class ActionFetchHoroscope(Action):
    def name(self):
        return "action_fetch_horoscope"

    def run(self, dispatcher, tracker, domain):

        # get horoscope from birth date and set slot for horoscopelist
         return [SlotSet("horoscopelist",horoscope)]


