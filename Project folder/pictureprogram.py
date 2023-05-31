import os
from picamera import PiCamera
import time



def take_picture():
    #Camera
    camera=PiCamera()
    camera.resolution=(64,64)
    camera.rotation=180

    #Folder
    path = "/home/pi/Project/kamerabilder"
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
    else:
        print("Exist folder")


    #Function
    fortsett = True

    counter = 0 #Counter to name the sample pictures
    while fortsett:
        userinput = input("Press ENTER to take picture or 1 to exit:")

        if userinput == "1":
            print("closing program")
            break;


        else:
            file_name="/home/pi/Project/kamerabilder/image" + str(counter) +".jpg"
            camera.capture(file_name)

            print("Picture taken")

            counter += 1