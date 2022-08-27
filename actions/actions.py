# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List, Union
from tkinter import EventType

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from storeDataInExcel_read import fetch_data
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, EventType
from storeDataInExcel_read import DataStore


class ActionShareURL(Action):

    def name(self) -> Text:
        return "action_share_url"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output=fetch_data(tracker.latest_message['entities'][3]['value'])
        dispatcher.utter_message(text="This is the data which you have asked for, \n{}".format(",".join(output)))
        return []


class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",first_name=tracker.get_slot("firstName"),
                                 last_name=tracker.get_slot("lastName"),mobile_number=tracker.get_slot("number"),
                                 Email_Id=tracker.get_slot("email"))
        DataStore(tracker.get_slot("firstName"), tracker.get_slot("lastName"), tracker.get_slot("number"),
                  tracker.get_slot("email"))

class FormDataCollect(Action):
    def name(self) -> Text:
        return "person_detail_form"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["firstName", "lastName", "number", "email"]

        for slot_name in required_slots:
            if tracker.get_slot(slot_name) is None:
                return [SlotSet("required_slots", slot_name)]

        return [SlotSet("required_slot", None)]

