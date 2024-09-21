import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic: #tao mic
    print("Robot: I'am listening")
    nghe = robot_ear.listen(mic) #nghe tu loa
    you = robot_ear.recognize_google(nghe) # chuyen tu nghe sang chu
    
    print('You: ', you)