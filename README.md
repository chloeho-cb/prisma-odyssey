# Triangle Game Installation Creative Embedded Sys

![Screen Recording 2024-03-21 at 11 29 59 AM (1)](https://github.com/chloeho7/triangle-world-game/assets/56209417/f77cb067-b08b-4130-b4b9-48913ebb355a)

Experimental Art Exploration Game Designed for 16-inch Macbook and Joystick (also supports WASD+SPACE controls and other sized screens) using [Pygame](https://www.pygame.org/)

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

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/12a3f3ff-0b4f-4a62-a33b-9cbeacb11e55" width="500">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/276436e0-cbf1-4424-97d8-c4c4968b6efd" width="500">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/9afbe4b5-1d09-46fd-a245-7092c0d92eec" width="500">
</div>

Measure and mark the dimensions for each piece on the balsa wood sheets according to the following specifications:
- 1 Back Panel: 2 5/8" x 1 5/16"
- 2 Side Triangles: Cut right triangle piece with a diagonal of 3 1/4" and a height of 1 7/8", and a base side measuring 2 5/8"
- 1 Door: 2 3/8" x 1 1/8" ( You can also measure this later using the gap between the two triangles peices)
- 1 Shelf Base: 1 1/4" x 1 1/4" ( Approx. Slightly Wider and Shorter than Base of Joystick )
- 1 Front Shelf Side: 1/2" x 1 1/4" 
- 2 Shelf Sides: 1 3/8" x 1/2"
- 2 Top Covers: 1/4" x 1 3/8"

#### Assembly
1. Lay out the pieces on a flat surface to ensure they fit together properly.
2. Set the Shelf Base on a flat surface and Glue the Front Shelf Side peice to one of the sides by aligning the edges of same length to create an L shape.
3. Glue the 2 Shelf Sides on parralel sides of the Shelf Base so the Side peices create a U shape on top of the Shelf Base peice.
4. Now check that the Joystick can fit between the sides and on top of the base. It should extend off the base.
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/85b99bce-f561-4ae8-aed4-b608166eff60" width="500">

5. Cover the Shelf Side Panel with glue on the side facing away from the other panel and attach to the triangle corner with long sides of the shelf sides in parallel to the 1 7/8" side of the triangle, and repeat with the other side & triangle.
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/86a0eb4a-d369-4873-bc74-4adf720f7a12" width="500">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/07001859-b795-4fc5-b5f5-c5592ce41dbf" width="500">
</div>
  
6. Glue the Back Panel between the Triangle peices by aligning the edges of the same length and gluing the edges.
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
<img src= "https://github.com/chloeho7/triangle-world-game/assets/56209417/610ffbf2-d343-45c0-b3f7-e4889097565b" width="500">
</div>
7. Glue a top cover on top of the connection between the 3 Shelf Sides.
8. Glue the other top cover at in parallel with the other top cover at the opposite end of the same side of the triangle.
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/9c684103-45e0-46db-9b9c-77d65aa3846a" width="500">

9. If you are okay with taking apart the enclosure to access the ESP32, (after connecting the joystick and ESP32) glue the door in the gap between the two triangles on the 2 5/8" side towards the shelf side such that there is a gap for the USB-C cord opposite of the joystick and shelving.
10. If you want to be able to access your ESP32 without taking apart the enclosure tape the door, use a hinge or attach leather peices evenly spaced along one of the long sides the door and attach the other end of each of the leather strips to the inside of the enclosure on a triangle. I reccomend attaching the leather / hinge on the opposite side of your dominant hand when looking at the gap, this way when you are holding the enclosure you hold the door closed.
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/d0466168-f65d-465c-ab2d-92c225730b0c" width="500">
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/7889c296-6390-4f54-863a-f93527892e7d" width="500">
</div>

### Connecting

- Joystick GND -> bottom right Ground on the TTGO
- Joystick 5V -> bottom right 5V
- Joystick VRx -> TTGO 27
- Joystick VRy -> TTGO 26
- Joystick SW -> TTGO 25
- Plug USB-C into computer and the ESP32
<img src="https://github.com/chloeho7/triangle-world-game/assets/56209417/a3e06335-a310-4a0a-958e-f93c3a05ea82" width="500">

### Credits

projection and movement from [here](https://stackoverflow.com/a/58675007)

Music: 
- Heavenly_ambience_NickR2020.wav by NickR2020 -- https://freesound.org/s/522053/ -- License: Attribution 3.0

SFX:
- Game FX #1 by danlucaz -- https://freesound.org/s/517755/ -- License: Creative Commons 0
- Time warp effect by chinomaker -- https://freesound.org/s/324644/ -- License: Creative Commons 0
