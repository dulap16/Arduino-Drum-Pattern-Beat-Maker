# Arduino 4 bar Drum pattern

## Part of an unnamed group of projects consisting of different apps that interact with Arduino components

### Description
4 Bar Drum Pattern Manager, Beat-Maker, similar to the FL Studio Channel Rec interface, but with arduino components
By pressing on a 4x4 button grid, you can select the beats on which a specific drum sound will play,
and then you can switch the sound or print out the entire pattern

### All the needed components for this group of projects can be found in the Arduino Uno R3 KIT with 24 components
### Required:
- Arduino Uno
- 2 Tact Buttons
- 4x4 Button Grid
- LCD 1602


**Lines that will be modified should you want to change sounds or add more sounds**
> script.py
```
# VARIABLES TO BE CHANGED
numberOfSounds = 5
List = [kick, hihat, clap, snare, openhat]
names = ["KICK", "HIHAT", "CLAP", "SNARE", "OPENHAT"]
```

> soundpad.ino
```
// CHANGE IF MORE SOUNDS ADDED
const int nrOfSounds = 5;
char sounds[20][20] = {"KICK", "HIHAT", "CLAP", "SNARE", "OPENHAT"};
```

Here you might need to change the lcd serial in the .ino or port in python
```
// I2C INITIALISATION
LiquidCrystal_I2C lcd(0x27, 16, 2);
```


## Setup
- the Arduino is provided the .ino, then it returns messages through the COM3 port (in my case) and the .py reads it and plays sounds
- you upload the .ino into the arduino, then close the arduino IDE and you don't have to do anything with it unless you want to add new sounds
- with the .py, you use the sounds you like (or the ones I used for a test), change the paths if needed
- with Arduino IDE closed and the Arduino Uno plugged in, run the .py and jam on the grid!


## Connecting the components - *coming soon*


## Adding and changing sounds
- all you need to do is change things in the parts of the code, both in the .ino and in the .py, that are preceded by messages saying that those are changeable parts
- when adding a new sound in .py, you need to write <yoursound> = pygame.mixer.Sound(r'<PATH>'), and then add <yoursound> to the List, and its name in caps to names
- change numberOfSounds (.py) and nrOfSounds (.ino) if needed
- the names list from the .py must be exactly the same as the sounds[20][20] from the .ino
- remember to add the correct paths to the .py


### That's about it. Have fun and feel free to criticize and offer feedback!
