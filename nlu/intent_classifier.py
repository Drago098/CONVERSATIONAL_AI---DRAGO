import yaml
from difflib import get_close_matches

class IntentClassifier:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.intents = yaml.safe_load(file)

    def classify(self, user_input):
        for intent, data in self.intents.items():
            if 'examples' in data:
                matches = get_close_matches(user_input.lower(), data['examples'], cutoff=0.6)
                if matches:
                    return intent
        return "default"
