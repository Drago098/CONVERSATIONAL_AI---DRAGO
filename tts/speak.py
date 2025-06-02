import pyttsx3

def speak(text):
    engine = pyttsx3.init(driverName='nsss')  # macOS native speech engine
    engine.say(text)
    engine.runAndWait()
