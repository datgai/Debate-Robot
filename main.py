# This is a sample Python script.

from bardapi import Bard
import requests


topics = ["Should Artificial Intelligence be used in university?","Do you need to have a college degree to get a good job?","Is technology making people less productive?"]

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
print("Debate Robot")

while True:
    starting = input("Hello I am XXX, would you like to debate with me?").upper()
    if starting == "Y":
        break
    else:
        continue


for topic in topics:
    print(topic)
chosenTopic = int(input("Please choose a topic! (1,3) "))
chosenTopic-=1
print(f"Chosen topic : {topics[chosenTopic]}")

#from now on rephrase your answer in a single paragraph summarization

# press CTRL+C to end infinite loop
while True:
    prompt = input("Enter your input: ")