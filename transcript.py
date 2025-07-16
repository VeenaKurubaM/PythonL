#install first pyttsx3 using pip command
import pyttsx3
engine=pyttsx3.init()
engine.say("Hi wlcome" + input("Enter name: "))
engine.runAndWait()
