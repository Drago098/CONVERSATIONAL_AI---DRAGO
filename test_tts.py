# test_tts.py
import pyttsx3

engine = pyttsx3.init(driverName='nsss')
engine.say("This is a test of the text to speech system.")
engine.runAndWait()

