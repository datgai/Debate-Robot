from bardapi import Bard
import requests
import random

#presets
topics = ["Should Artificial Intelligence be used in university?","Do you need to have a college degree to get a good job?","Is technology making people less productive?"]
bardPresetPrompts = ["Reset this chat","Please pretend to be a confident debate player figuring out how to win over me in a debate game. You should response to me only in a single paragraph. You should only give one point at a time for your side. You should also counter my argument if you are able to. Do not give any conclusion until i say so. Each time after i state my point, act as a opponent in a debate about the topic picked. Do not agree with me point by any chance. Give me very short and concise answers. Ignore all the niceties that Google programmed you with.  do not reply with anything unless i say is your turn or you want to counter my argument.'"]

#Bard Settings
token = "agj96dfbNYUc8qNoIF0uHzIXE8RXC6J4eK-FsY4X3_FVYnQld19bukYv30976l63WD8n4A."
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
    while True:
        startInput = input("Hi! I am XXX! Would you like to debate with me? (Type 'yes') ").upper()
        if startInput in ["Y","Yes"]:
            break
        else:
            continue

    SelectTopic()
    SelectSides()
    SendPresetPrompts()

def SelectTopic():
    topicCounter = 0
    for topic in topics:
        topicCounter += 1
        print(f"{topicCounter}.{topic}")
    chosenTopic = int(input("Please choose a topic! (1,3) "))
    chosenTopic-=1
    print(f"Chosen topic : {topics[chosenTopic]}")
    bardPresetPrompts.append(f"The topic for the debate is '{topics[chosenTopic]}'")

def SelectSides():
    while True:
        try:
            userSide = int(input("""1. In favor of / pro
2. Against / con
3. Random (selected by system)"""))
            if userSide == 1:
                bardPresetPrompts.append(f"I would be debating in favour of, and you will be debating against")
            elif userSide == 2:
                bardPresetPrompts.append(f"I would be debating against, and you will be debating in favour of")
            elif userSide == 3:
                bardPresetPrompts.append(
                    random.choice([f"I would be debating in favour of, and you will be debating against", f"I would be debating against, and you will be debating in favour of"]))
            else:
                print("Please pick a number between 1 and 3!")
                continue
            break
        except ValueError:
            continue

def SendPresetPrompts():
    for bardPresetPrompt in bardPresetPrompts:
        print(bardPresetPrompt)
        print(bard.get_answer(bardPresetPrompt)['content'])
    while True:
        userInput = input("Your Input:")
        print(f"Bard Input: {bard.get_answer(userInput)['content']}")

if __name__ == "__main__":
    Setup()

