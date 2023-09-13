import speech_recognition as sr
import time



r = sr.Recognizer()
r.energy_threshold = 100

with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    start = time.time()
    print("Calculating...")
    try:
        print("Whisper thinks you said " + r.recognize_whisper(audio, language="english"))
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")

    end = time.time()
    print(f"Processing Time : {end - start}")