import pyttsx3
import speech_recognition
from datetime import date,datetime

# khởi tạo biến
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
   
while True:  
    # code tiếp nhận giọng nói
    with speech_recognition.Microphone() as mic: #tao mic
        print("Robot: I'am listening")
        nghe = robot_ear.listen(mic) #nghe tu mic
    try:
        audio = robot_ear.recognize_google(nghe) # chuyen tu nghe sang chu    
    except:
        audio = ""

    print(audio)

    # code phương án trả lời
    if 'hello' in audio:
        robot_brain = 'hello Master'
    elif 'today' in audio:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif 'time' in audio:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M Minutes %S seconds")
    elif 'bye' in audio:
        robot_brain = 'good night, Master'
        print("AI: ",robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Sorry, I cant hear you saying anything"

    # AI đáp lại
    print("AI: ",robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
