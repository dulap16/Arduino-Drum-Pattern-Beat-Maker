# Arduino 4 bar Drum pattern

## Part of an unnamed group of projects consisting of different apps that interact with Arduino components
### All the needed components for this group of projects can be found in the Arduino Uno R3 KIT with 24 components

This is a drum 4 bar pattern manager with arduino components as an interface 
Each button on the grid coresponds to a beat, and the sound can be changed by pressing a button, 
therefore you can create diverse beats as an interesting project with an interesting interface


### Required: ARDUINO UNO; 2 BUTTONS; 4X4 BUTTON GRID; LCD 1602
- Arduino Uno
- 2 Tact Buttons
- 4x4 Button Grid
- LCD 1602


This is an FL Studio Channel REC type app that makes use of Arduino components to make a user-friendly and fun interface
This makes for a cool project as having physical buttons to press is much more interactive and interesting
The lcd component is also pretty cool, but it can be skipped as you can also see the entire beat in your IDE by pressing one of the buttons

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


## How it works
- the Arduino is provided the .ino, then it returns messages through the COM3 port (in my case) and the .py reads it and plays sounds
- you upload the .ino into the arduino, then close the arduino IDE and you don't have to do anything with it unless you want to add new sounds
- with the .py, you use the sounds you like (or the ones I used for a test), change the paths if needed
- with arduino IDE closed and the arduino plugged in, run the .py and jam on the grid!


## Connecting the components - *coming soon*


## Adding and changing sounds
- all you need to do is change things in the parts of the code, both in the .ino and in the .py, that are preceded by messages saying that those are changeable parts
- when adding a new sound in .py, you need to write <yoursound> = pygame.mixer.Sound(r'<PATH>'), and then add <yoursound> to the List, and its name in caps to names
- change numberOfSounds (.py) and nrOfSounds (.ino) if needed
- the names list from the .py must be exactly the same as the sounds[20][20] from the .ino
- remember to add the correct paths to the .py


### That's about it. Have fun and feel free to criticize and offer feedback!
