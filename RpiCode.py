
import RPi.GPIO as GPIO

import time, pygame

import os


pygame.init()

pygame.mixer.init()

file=("/home/pi/Desktop/ForgotttenItem.mp3")



GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN) #read gpio 17 pin



while 1:
    
    os.system("sudo /home/pi/433Utils/RPi_utils/RFSniffer >outputs.txt & pkill --signal SIGINT RFSniffer")

    f=open("outputs.txt","r")

    readf = f.read()

    print(readf)

    if "2" in readf:

        print("item detected in box")

        PIR=GPIO.input(17)

        print(PIR)

        if PIR==1:

            print("presence detected at door")

            time.sleep(1)

            pygame.mixer.music.load(file)

            pygame.mixer.music.play()

        if f.closed == "False":

            f.close()

        time.sleep(10)

    else:

        print("nothing in the box")

        if f.closed == "False":

            f.close()

            os.remove("outputs.txt")

            time.sleep(1)
