import pyttsx4
import time

t = int(time.strftime("%H"))
print(t)
a = pyttsx4.init()

if t >= 6 and t < 12:
    a.say("Good morning sir")

elif t >= 12 and t < 16:
    a.say("Good afternoon sir")

elif t >= 16 and t < 20:
    a.say("Good evening sir")

elif t >= 20 or t < 6:
    a.say("Good night sir")

a.runAndWait()