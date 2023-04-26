import serial.tools.list_ports
from pydub import AudioSegment
from pydub.playback import play
import pygame
from threading import Thread
import ffmpeg
import json
import time


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
pygame.init()
pygame.mixer.init()


# READ CONFIG
pathToConfig = __file__[:-9] + "\config.json"
with open(pathToConfig, "r") as jsonfile:
    data = json.load(jsonfile)
sounds = data['sounds']
paths = data['paths']


# SOUND PATHS
soundPath = __file__[:-9] + '\sounds\\'

cmd = ""
List = []
numberOfSounds = len(sounds)
for i in range(0, len(paths)):
    List.append(pygame.mixer.Sound(soundPath + paths[i]))
    cmd = cmd + sounds[i] + " "

cmd = cmd[:-1]
cmd = cmd + '\r'
print(cmd)


soundMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

soundsPlayed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def music():
    while True:
        for beat in range(1, 17):

            for sound in range(0, numberOfSounds):
                if(soundMatrix[sound][beat]):
                    soundsPlayed[sound] = 1
            
            for i in range(0, numberOfSounds):
                if soundsPlayed[i] == 1:
                    List[i].play()
                soundsPlayed[i] = 0
            time.sleep(0.2)

def equalizeLines(word):
    l = len(word)

    return lengthiestOutOfSounds() - l

def lengthiestOutOfSounds():
    maxi = 0
    for i in range(0, numberOfSounds):
        maxi = max(maxi, len(sounds[i]))
    
    return maxi


def readSerial():

    serialInst.baudrate = 9600
    serialInst.port = "COM3"
    serialInst.open()
    
    time.sleep(2)
    serialInst.write(cmd.encode())

    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            line = (packet.decode('utf')).rstrip('\n')

            if line[0] >= '0' and line[0] <= '9':
                first, second = line.split(' ')
                row = int(first)
                column = int(second)

                if soundMatrix[row][column] == True:
                    soundMatrix[row][column] = False
                else: 
                    soundMatrix[row][column] = True
            else:
                tokens = line.split(' ')

                ok = False
                for i in range(0, numberOfSounds):
                    if tokens[0] == sounds[i]:
                        ok = True
                        i = numberOfSounds

                if ok == True:
                    print(tokens[0], end = " ", flush = True)

                    spaces = equalizeLines(tokens[0])
                    print(" " * spaces, end = "", flush = True)

                    for i in range(1, 17):
                        if tokens[i] == '1': 
                            print("▮", end = "", flush = True)
                        else: print("▯", end = "", flush = True)
                    print()
                
                if tokens[0] == sounds[numberOfSounds - 1]:
                    print()
                    print()


if __name__ == "__main__":
    read = Thread(target = readSerial)
    makeMusic = Thread(target = music)

    read.start()
    makeMusic.start()

    serialInst.close()