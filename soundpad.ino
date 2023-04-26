#include <Wire.h>
#include <Keypad.h>
#include <LiquidCrystal_I2C.h>
#include <ArduinoJson.h>
#include <string.h>

#define changeSoundInput A0
#define printBeatInput A1
#define changeSoundOutput 13
#define printBeatOutput 12

char printedSound[20];

// 4X4 KEYPAD INITIALISATION
const byte ROWS = 4;
const byte COLS = 4;

byte cols[COLS] = {5, 4, 3, 2}; // COLUMN PINS
byte rows[ROWS] = {6, 7, 8, 9}; // ROW PINS
char keys[ROWS][COLS] = {
  {'1', '2', '3', '4'}, 
  {'5', '6', '7', '8'}, 
  {'9', 'A', 'B', 'C'}, 
  {'D', 'E', 'F', 'G'}, 
};

Keypad keypad = Keypad(makeKeymap(keys), rows, cols, ROWS, COLS);

// I2C INITIALISATION
LiquidCrystal_I2C lcd(0x27, 16, 2);


int currentSound = 0;
bool soundMatrix[20][17];

bool changeOff = true;
bool showGridOff = true;
int timer = 0;

bool receivedMessage = false;
String mycmd;

int nrOfSounds = 0;
String strsounds[20];
char sounds[20][20];

void setup() {
  Serial.begin(9600);

  pinMode(changeSoundOutput, OUTPUT);
  pinMode(printBeatOutput, OUTPUT);

  digitalWrite(changeSoundOutput, HIGH);
  digitalWrite(printBeatOutput, HIGH);



  // READ SERIAL
  while(Serial.available() == 0)
  {

  }

  receivedMessage = true;
  mycmd = Serial.readStringUntil('\r');

  while (mycmd.length() > 0)
  {
    int index = mycmd.indexOf(' ');
    if (index == -1) // No space found
    {
      strsounds[nrOfSounds++] = mycmd;
      break;
    }
    else
    {
      strsounds[nrOfSounds++] = mycmd.substring(0, index);
      mycmd = mycmd.substring(index+1);
    }
  }

  for(int i = 0; i < nrOfSounds; i++) {
    strsounds[i].toCharArray(sounds[i], strsounds[i].length() + 1);
  }

  
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print(sounds[0]);
}

void loop() {

  char pressed = keypad.getKey();

  if(pressed) {
    int i = hexaToInt(pressed);
    Serial.print(currentSound);
    Serial.print(" ");
    Serial.println(hexaToInt(pressed));
    soundMatrix[currentSound][i] = !(soundMatrix[currentSound][i]);

    lcd.setCursor(i - 1, 1);
    if(soundMatrix[currentSound][i])
      lcd.write(255);
    else lcd.print(" ");
  }

  if(analogRead(changeSoundInput))
  {
    if(changeOff) {
      changeOff = false;
      currentSound = (currentSound + 1) % nrOfSounds;

      // CHANGE DISPLAY

      lcd.setCursor(0, 0);
      strcpy(printedSound, sounds[currentSound]);
      strcat(printedSound, "   ");
      lcd.print(printedSound);

      
      for(int i = 1; i <= 16; i++)
      {
        lcd.setCursor(i - 1, 1);
        if(soundMatrix[currentSound][i])
          lcd.write(255);
        else lcd.print(" ");
      }

      Serial.println();
    }
  } else changeOff = true;

  if(analogRead(printBeatInput))
  {
    if(showGridOff) {
      showGridOff = false;
      printSounds();
    }
  } else showGridOff = true;

  delay(10);
}

int hexaToInt(char c)
{
  if(c >= 'A')
    return c - 'A' + 10;
  return c - '0';
}

void printSounds()
{
  for(int i = 0; i < nrOfSounds; i++)
  {
    Serial.print(sounds[i]);
    Serial.print(" ");
    for(int j = 1; j <= 16; j++) {
      Serial.print(soundMatrix[i][j]);
      Serial.print(" ");
    }
    Serial.println();
  }
  Serial.println();
}
