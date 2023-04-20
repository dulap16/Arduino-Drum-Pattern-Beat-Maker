# Beat-Maker-3000
Drum 4 bars pattern manager with arduino components as an interface 
Each button on the grid coresponds to a beat, and the sound can be changed by pressing a button, therefore you can create diverse beats as an interesting project with an interesting interface

NEED : ARDUINO UNO; 2 BUTTONS; 4X4 BUTTON GRID; LCD 1602

This is a FL Studio Channel REC type app that makes use of Arduino components to make a user-friendly and fun interface
This makes for a cool project as having physical buttons to press is much more interactive and interesting
The lcd component is also pretty cool, but it can be skipped as you can also see the entire beat in your IDE by pressing one of the buttons

ALL PARTS OF THE ARDUINO AND PYTHON CODE THAT NEED TO BE CHANGED ARE PRECEDED BY A MESSAGE 
( you might need to change the lcd serial in the .ino or port in python )

HOW IT WORKS 
-> the Arduino is given the .ino, then it returns messages through the COM3 port ( in my case ) and the .py reads it and plays sounds
- you upload the .ino into the arduino, then close the arduino IDE and you don't have to do anything with it unless you want to add new sounds
- with the .py, you use the sounds you like ( or the ones I used for a test ), change the paths if needed
- with arduino IDE closed and the arduino plugged in, run the .py and jam on the grid!


CONNECTING THE ARDUINO COMPONENTS - coming soon
The connections as I made them are the following way:
LCD
- blah


ADDING AND CHANGING SOUNDS
- all you need to do is change things in the parts of the code, both in the .ino and in the .py, that are preceded by messages saying that those are changeable parts
- when adding a new sound in .py, you need to write <yoursound> = pygame.mixer.Sound(r'<PATH>'), and then add <yoursound> to the List, and its name in caps to names
- change numberOfSounds (.py) and nrOfSounds (.ino) if needed
- the names list from the .py must be exactly the same as the sounds[20][20] from the .ino
- remember to add the correct paths to the .py

That's about it. Have fun!
