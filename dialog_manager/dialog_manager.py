from datetime import datetime
import yaml
import random

class DialogManager:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.intents = yaml.safe_load(file)

    def get_response(self, intent):
        responses = self.intents.get(intent, {}).get('response', [])
        if not responses:
            return "I'm not sure how to respond to that."

        # Choose a random response from the list
        response = random.choice(responses)

        # Replace dynamic placeholders
        if "{time}" in response:
            response = response.replace("{time}", datetime.now().strftime("%H:%M:%S"))
        if "{date}" in response:
            response = response.replace("{date}", datetime.now().strftime("%A, %d %B %Y"))
        if "{weather}" in response:
            response = response.replace("{weather}", "sunny and 28°C")  # hardcoded for now
        if "{events}" in response:
            response = response.replace("{events}", "a meeting at 10 AM and a dentist appointment at 4 PM")

        return response
