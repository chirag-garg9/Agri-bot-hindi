# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import os
class ActionHandleQuickReply(Action):
    def name(self) -> Text:
        return "Scheme_details"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        # Get the user's selected option from the payload
        words = tracker.latest_message
        scheme_name = tracker.latest_message.get('entities', [{'entity': 'scheme_name'}])[0]['value']
        scheme_name = scheme_name.lower().split(" ")
        confidence = []
        schemes = []
        l=os.listdir('./Schemes')
        for i in l:
            schemes.append(i.split('.')[0].lower().split(" "))

        for i in schemes:
            confidence.append(len(set(i).intersection(set(scheme_name))))

        file_name = l[confidence.index(max(confidence))]

        # Specify the file path
        file_path = f"./Schemes/{file_name}"

        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read and print each line while preserving indentation
            for line in file:
                dispatcher.utter_message(f"{line}")
        return []

