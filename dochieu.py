import time
you=input()
if you == 'hello':
    robot_brain = 'hello Master'
elif you == 'today':
    named_tuple = time.localtime() # get struct_time
    robot_brain = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
elif you == 'bye':
    robot_brain = 'good night'
else:
    robot_brain = "I'cant hear you saying anything"
print(robot_brain)
    