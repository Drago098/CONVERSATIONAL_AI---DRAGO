from nlu.intent_classifier import IntentClassifier
from dialog_manager.dialog_manager import DialogManager
from tts.speak import speak

WAKE_WORD = "drago"

def main():
    classifier = IntentClassifier("config/intents.yaml")
    manager = DialogManager("config/intents.yaml")

    print("🧠 Drago is online! Say something like 'Drago, what's the weather in Delhi?'")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🧠 Drago: Shutting down. Goodbye!")
            break

        if WAKE_WORD in user_input.lower():
            cleaned_input = user_input.lower().replace(WAKE_WORD, "").strip()
            intent = classifier.classify(cleaned_input)
            response = manager.get_response(intent, cleaned_input)  # ✅ FIXED HERE
            print("🧠 Drago:", response)
            speak(response)
        else:
            print("🧠 Drago: Say my name if you need me.")

if __name__ == "__main__":
    main()
