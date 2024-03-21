# Triangle Game Installation Creative Embedded Sys

![Screen Recording 2024-03-21 at 11 29 59 AM (1)](https://github.com/chloeho7/triangle-world-game/assets/56209417/f77cb067-b08b-4130-b4b9-48913ebb355a)


projection and movement from [here](https://stackoverflow.com/a/58675007)

Music: 
- Heavenly_ambience_NickR2020.wav by NickR2020 -- https://freesound.org/s/522053/ -- License: Attribution 3.0


SFX:
- Game FX #1 by danlucaz -- https://freesound.org/s/517755/ -- License: Creative Commons 0
- Time warp effect by chinomaker -- https://freesound.org/s/324644/ -- License: Creative Commons 0

Designed for 16-inch Macbook and joystick also supports WASD+SPACE controls

## Playing the game
1. Clone this repo and `cd` into the created directory
2. `python3 trianglegame.py`

To play with the Joystick, it needs to be connected before launching game and will crash the game if disconnected mid game

## How to recreate / play using the joystick

You do not need the following to play using the keyboard

### Components
- TTGO T-display ESP32
- USB-C
- Machine that supports [Arduino IDE](https://www.arduino.cc/en/software)
- Joystick 
- 5 Female to Female Wires
#### Enclosure Components
- 1/16" x 4" x 12" Basswood (can also use balsawood, cardboard, etc.)
- Wood glue (or super glue, hot glue etc. depending on materials)
- Scissors
- Measuring Tool
- Leather & Leather glue (optional)

### IDE and libraries
1. [Download Arduino IDE](https://www.arduino.cc/en/software)
2. Launch the IDE and open the Settings/Preferences page: Ardunio --> Settings
3. Copy and paste, https://dl.espressif.com/dl/package_esp32_index.json, into Additional Boards Manager URLs

### Download Code and Upload to ESP32
1. Download [`joystick.ino`](https://github.com/chloeho7/triangle-world-game/blob/d5ca7c725207c7df5d2a77c19f493d36d7b9a1ea/joystick.ino) and open in the file in the [Arduino IDE](https://www.arduino.cc/en/software)
2. Connect the TTGO T-display ESP32 and your computer using the USB-C
3. In the [Arduino IDE](https://www.arduino.cc/en/software) select Tools and the corresponding Port
4. Select Upload

### Enclosure 

### Connecting

