
import pyttsx3
import os


pyttsx3.speak("hello Mr. Bardhan Welcome to stark expo plz chat with me i am jarvis in your service")

while True:

	print("enter your choice :" ,end=" ")	
	p = input()
#print(p)
#os.system(p)

	if ("hey" in p ) or ("hii" in p) or ("hi" in p) or ("hello" in p):
		pyttsx3.speak("hii sir how are u")

	elif ("you" in p) or ("how" in p) or ("fine" in p):
		pyttsx3.speak("i am fine sir how may i help you ")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("chrome" in p):
		pyttsx3.speak("sure Mr. bardhan here we go for google chrome")
		os.system("start chrome")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("notepad" in p) or ("editor" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for notepad editor")
		os.system("notepad")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("cmd" in p) or ("command prompt" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for command prompt")
		os.system("cmd")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("cal" in p) or ("calculator prompt" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for calculator")
		os.system("calc")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("task" in p) or ("manager" in p) or ("mgr" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for task manager")
		os.system("taskmgr")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and ("paint" in p):	
		pyttsx3.speak("sure Mr. bardhan here we go for paint")
		os.system("mspaint")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("word" in p) or ("msword" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for microsoft word")
		os.system("start winword")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("excel" in p) or ("msexcel" in p)):	
		pyttsx3.speak("sure Mr. bardhan here we go for microsoft excel")
		os.system("start excel")

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) ) and (("media" in p) or ("player" in p)):
		pyttsx3.speak("sure Mr. bardhan here we go for window media player")
		os.system("wmplayer")

	elif (("exit" in p) or ("q" in p) or ("quit" in p)):
		pyttsx3.speak("ok Mr. Bardhan take care  ")
		break
	else:
		pyttsx3.speak("unsuported")