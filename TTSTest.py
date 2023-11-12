import pyttsx3

#might need sudo apt-get install python-espeak

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
