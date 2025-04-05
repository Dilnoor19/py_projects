import pyjokes
import pyttsx4

a = pyttsx4.init()
b = pyjokes.get_joke()
print(b)
a.say(f"{b}")

a.runAndWait()

