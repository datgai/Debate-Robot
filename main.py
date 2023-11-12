import speech_recognition as sr

from bardapi import Bard
import requests
import random

from gtts import gTTS


#presets
topics = ["Should Artificial Intelligence be used in university?","Do you need to have a college degree to get a good job?","Is technology making people less productive?"]
bardPresetPrompts = ["Reset this chat","Please pretend to be a confident debate player figuring out how to win over me in a debate game. You should response to me only in a single paragraph. You should only give one point at a time for your side. You should also counter my argument if you are able to. Do not give any conclusion until i say so. Each time after i state my point, act as a opponent in a debate about the topic picked. Do not agree with me point by any chance. Give me very short and concise answers. Ignore all the niceties that Google programmed you with.  do not reply with anything unless i say is your turn or you want to counter my argument.'"]

#Bard Settings
token = "dAj96TgLM0CCppJHOGyq__4Rw2Oqy7O_J93r8NGsMZnAapV-KZ4oNubz2AcrKRszAQKOpQ."
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }


session.cookies.set("__Secure-1PSID", token)
bard = Bard(token=token, session=session, timeout=30)

def Setup():
    '''kinda the main function'''
    while True:
        print("Hi! I am XXX! Would you like to debate with me? (Type 'yes') ")
        try:
            startInput = SpeechRecognition()
        except Exception:
            print("ERROR LOOP")
            continue

        if startInput.upper() in ["Y","YES"]:
            break
        else:
            print("ERROR LOOP")
            continue

    SelectTopic()
    SelectSides()
    SendPresetPrompts()
    PromptLoop()

def SelectTopic():
    '''select from one of the 3 topics'''
    while True:
        try:
            topicCounter = 0
            for topic in topics:
                topicCounter += 1
                print(f"{topicCounter}.{topic}")
            print("Please choose a topic! (Choose a number from '1' to '3'!)")

            try:
                chosenTopic = SpeechRecognition()
                int(chosenTopic)
            except Exception:
                chosenTopic = ConvertSelectionToInt(chosenTopic)

            chosenTopic-=1
            print(f"Chosen topic : {topics[chosenTopic]}")
            bardPresetPrompts.append(f"The topic for the debate is '{topics[chosenTopic]}'")
            break
        except Exception as e:
            print(e)
            print("ERROR LOOP")
            continue

def SelectSides():
    ''' select which side are you on'''
    while True:
        print("""1. In favor of / pro
2. Against / con
3. Random (selected by system)""")

        try:
            userSide = SpeechRecognition()
            int(userSide)
        except Exception:
            userSide = ConvertSelectionToInt(userSide)

        if userSide == 1:
            bardPresetPrompts.append(f"I would be debating in favour of, and you will be debating against")
        elif userSide == 2:
            bardPresetPrompts.append(f"I would be debating against, and you will be debating in favour of")
        elif userSide == 3:
            bardPresetPrompts.append(random.choice([f"I would be debating in favour of, and you will be debating against", f"I would be debating against, and you will be debating in favour of"]))
        else:
            print("Please pick a number between 1 and 3!")
            print("ERROR LOOP")
            continue
        break

def SendPresetPrompts():
    '''send the setting prompts to bards'''
    for bardPresetPrompt in bardPresetPrompts:
        print(bardPresetPrompt)
        print(bard.get_answer(bardPresetPrompt)['content'])

def PromptLoop():
    while True:
        userInput = SpeechRecognition()
        print(f"Bard Input: {bard.get_answer(userInput)['content']}")

def SpeechRecognition():
    r = sr.Recognizer()
    r.energy_threshold = 1800

    while True:
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)


        try:
            print(f"User input: {r.recognize_google(audio)}")
            return r.recognize_google(audio)
            break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            print("ERROR LOOP")
            continue
        except sr.RequestError as e:
            raise ("Could not request results from Google Speech Recognition service; {0}".format(e))


def ConvertSelectionToInt(selection):
    '''helper function to convert to int'''
    if 'one' in selection:
        return 1
    elif 'two' in selection:
        return 2
    elif 'three' in selection:
        return 3
    else:
        print(selection)
        return "Please pick a number between 1 and 3!"

if __name__ == "__main__":
    Setup()

