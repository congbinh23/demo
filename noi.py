import pyttsx3
import time
robot_mouth = pyttsx3.init()
robot_mouth.say('Python has built-in support for putting your program to sleep. The time module has a function sleep() that you can use to suspend execution of the calling thread for however many seconds you specify.')
robot_mouth.runAndWait()
time.sleep(0.4)
robot_mouth.say('Hello, how are you today!?')
robot_mouth.runAndWait()