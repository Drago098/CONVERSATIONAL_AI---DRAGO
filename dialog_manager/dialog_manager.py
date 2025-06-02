from datetime import datetime
import yaml
import random
import re
from actions.weather import get_weather  # real weather function

class DialogManager:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.intents = yaml.safe_load(file)

    def extract_city(self, text):
        match = re.search(r"in ([a-zA-Z\s]+)", text.lower())
        return match.group(1).strip() if match else "Rourkela"

    def get_response(self, intent, user_input=""):
        responses = self.intents.get(intent, {}).get('response', [])
        if not responses:
            return "I'm not sure how to respond to that."

        response = random.choice(responses)

        # Replace dynamic placeholders
        if "{time}" in response:
            response = response.replace("{time}", datetime.now().strftime("%H:%M:%S"))
        if "{date}" in response:
            response = response.replace("{date}", datetime.now().strftime("%A, %d %B %Y"))
        if "{weather}" in response:
            city = self.extract_city(user_input)
            weather_info = get_weather(city)
            response = response.replace("{weather}", weather_info)
        if "{events}" in response:
            response = response.replace("{events}", "a meeting at 10 AM and a dentist appointment at 4 PM")

        return response
