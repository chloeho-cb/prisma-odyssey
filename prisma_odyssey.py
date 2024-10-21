import pygame
from pygame import mixer
from pygame.locals import *
import random
import numpy as np
import math
import serial
import os
import webbrowser

pygame.init()
run=True

random.seed()

s = 'sound'
mixer.init()
music = mixer.music.load(os.path.join(s, '522053__nickr2020__heavenly_ambience_nickr2020.wav'))
# Heavenly_ambience_NickR2020.wav by NickR2020 -- https://freesound.org/s/522053/ -- License: Attribution 3.0
mixer.music.play(-1)
captured = mixer.Sound(os.path.join(s, '517755__danlucaz__game-fx-1.wav'))
# Game FX #1 by danlucaz -- https://freesound.org/s/517755/ -- License: Creative Commons 0
complete = mixer.Sound(os.path.join(s, '324644__chinomaker__time-warp-effect.wav'))
# Time warp effect by chinomaker -- https://freesound.org/s/324644/ -- License: Creative Commons 0

# Serial communication setup
port = '/dev/cu.usbserial-56230321241'
try:
    ser = serial.Serial(port, 115200)  # Adjust COM port as necessary
except Exception:
    ser = False
    pass

#screensize
screensize = (width,height)=(pygame.display.Info().current_w,pygame.display.Info().current_h-120)#(1000,1000)
center=(int(width/2),int(height/2))
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Prisma Odyssey')

#delta mov
ds=10
do=0.01

reds = [(255, 0, 0), (200, 0, 0), (150, 0, 0), (100, 0, 0), (50, 0, 0)]
oranges = [(255, 127, 80),(242, 140, 40),(255, 100, 0),(255, 95, 31),(255, 69, 0)] 
yellows = [(255, 255, 0), (215, 200, 0), (230, 200, 0), (200, 200, 0), (250, 200, 0)]
greens = [(0, 255, 0), (0, 200, 0), (0, 150, 0), (0, 100, 0), (0, 50, 0)]
blues = [(0, 0, 255), (0, 0, 200), (0, 0, 150), (0, 0, 100), (0, 0, 50)]
purples = [(207, 159, 255),(195, 177, 225),(128, 0, 128),(127, 0, 255),(93, 63, 211)]
colors = [reds, oranges, yellows, greens, blues, purples]

maincolor = greens
secondarycolor = blues

def draw_complete(target, colors, n, big=False):
    angle = 360 / target
    x0, y0 = 70, 70
    side_length = 200 // 2 - 50
    if big:
        x0, y0 = center
        side_length = 1000 // 2 - 50
    
    for i in range(n):
        color = colors[i % len(colors)]
        # Calculate the vertices of the triangle
        x1 = x0 + side_length * math.cos(math.radians(i * angle))
        y1 = y0 + side_length * math.sin(math.radians(i * angle))
        x2 = x0 + side_length * math.cos(math.radians((i + 1) * angle))
        y2 = y0 + side_length * math.sin(math.radians((i + 1) * angle))
        
        # Draw and fill the triangle
        pygame.draw.polygon(screen, color, [(x0, y0), (x1, y1), (x2, y2)])
        
    # Draw the border lines
    for i in range(target):
        x1 = x0 + side_length * math.cos(math.radians(i * angle))
        y1 = y0 + side_length * math.sin(math.radians(i * angle))
        x2 = x0 + side_length * math.cos(math.radians((i + 1) * angle))
        y2 = y0 + side_length * math.sin(math.radians((i + 1) * angle))
        color = colors[i % len(colors)]
        pygame.draw.lines(screen, color, True, [(x0, y0), (x1, y1), (x2, y2)], 4)

def get_initial_points(target, maincolor=greens, secondarycolor=blues):
    points = []
    for i in range(2000):
        n1 = random.randrange(-10000, 10000)
        n2 = random.randrange(-10000, 10000)
        n3 = random.randrange(-10000, 10000)
        rand = random.randrange(10, 700)
        points.append([n1, n2, n3, rand, random.choice(maincolor)])

    for i in range(target):
        n1 = random.randrange(100, 1000)  
        n2 = 0 
        n3 = random.randrange(100, 5000)  
        rand = random.randrange(30, 500)
        points.append([n1, n2, n3, rand, random.choice(secondarycolor)])
    
    return points

def move_forward():
    for p in points:
        p[2]-=ds

def move_backward():
    for p in points:
        p[2] += ds

def move_left():
    for p in points:
        p[0], p[2] = np.cos(-do) * p[0] - np.sin(-do) * p[2], np.sin(-do) * p[0] + np.cos(-do) * p[2]

def move_right():
     for p in points:
        p[0], p[2] = np.cos(do) * p[0] - np.sin(do) * p[2], np.sin(do) * p[0] + np.cos(do) * p[2]


FPS = 30
clock = pygame.time.Clock()

target = 3
points = get_initial_points(target)
count = 0
joystick_x, joystick_y = 1950, 1950
button_val = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    ########## joystick
    if ser:
        data = ser.read(ser.inWaiting() or 1).decode('utf-8', errors='ignore')
        if data:
            try:
                joystick_x, joystick_y, button_val = (int(value) for value in data.strip().split(','))
            except ValueError:
                pass

    ################## keys
    keys=pygame.key.get_pressed()

    if joystick_y > 2000 or keys[pygame.K_w]:
        move_forward()
    elif joystick_y < 1900 or keys[pygame.K_s]:
        move_backward()

    if joystick_x < 1900 or keys[pygame.K_a]:
        move_left()
    elif joystick_x > 2000 or keys[pygame.K_d]:
        move_right()

    ############################### Collision detection and projection ###################

    screen.fill((0,0,0))
    for p in points:
        #this is to create new stars
        if p[2]<=-5000 or p[2]>=5000:
            p[0], p[1], p[2] = random.randrange(-10000,10000), random.randrange(-10000,10000), random.randrange(1000,10000)  
            if not p[4] in secondarycolor:
                p[3] = random.randrange(10,700)
                p[4] = random.choice(maincolor)  
        else:
            #this is to ignore stars which are behind the ship
            if p[2]<=0:
                pass
            else:
                w = p[2] * 30 / 5000
                rand = p[3]
                angle = p[2] / 5000 * np.pi  # Calculate rotation angle based on z-coordinate
                vertices = [(int(p[0]/w+center[0]), int(p[1]/w+center[1])-rand/w),
                            (int(p[0]/w+center[0])-rand/w, int(p[1]/w+center[1])+rand/w),
                            (int(p[0]/w+center[0])+rand/w, int(p[1]/w+center[1])+rand/w)]
                rotated_vertices = [(int((v[0]-center[0])*np.cos(angle) - (v[1]-center[1])*np.sin(angle) + center[0]),
                                     int((v[0]-center[0])*np.sin(angle) + (v[1]-center[1])*np.cos(angle) + center[1]))
                                    for v in vertices]  # Rotate the vertices
                # skip if triangle is outside the screen boundaries
                if all(v[0] < 0 or v[0] > screensize[0] or v[1] < 0 or v[1] > screensize[1] for v in rotated_vertices):
                    continue  
                pygame.draw.polygon(screen, p[4], rotated_vertices)  # Use p[4] as the color parameter
                if p[4] in secondarycolor:
                    triangle_area = abs((rotated_vertices[0][0] * (rotated_vertices[1][1] - rotated_vertices[2][1]) +
                                        rotated_vertices[1][0] * (rotated_vertices[2][1] - rotated_vertices[0][1]) +
                                        rotated_vertices[2][0] * (rotated_vertices[0][1] - rotated_vertices[1][1])) / 2)
                    screen_area = screensize[0] * screensize[1]
                    if triangle_area > screen_area * 0.01 and (button_val or keys[pygame.K_SPACE]): # detect collision
                        count += 1 # increment count of found triangles
                        mixer.Sound.play(captured)
                        if p in points:
                            points.remove(p)
                        if count == target: # reset the game
                            mixer.Sound.play(complete)
                            draw_complete(target, secondarycolor, count, big=True)
                            font = pygame.font.Font(None, 200)
                            count_text = font.render(f"{count}", True, (255, 255, 255))
                            screen.blit(count_text, (center[0]-50,center[1]-70))
                            pygame.display.update()
                            if target == 3:
                                   webbrowser.open("https://dynamic-qr.linkdrop.io/#/mqr/6Fs6FuUzqS1q/J6SJ6s5zxRAf",new=0, autoraise=True)
                            count = 0
                            target += 1
                            choices = colors.copy()
                            if len(maincolor) > 5: # remove the color that was used
                                maincolor = maincolor[5:]
                            maincolor += secondarycolor # add the color that collected to the main color list
                            secondarycolor = random.choice(choices) # choose a new secondary color
                            while any(x in secondarycolor for x in maincolor):
                                secondarycolor = random.choice(choices)
                            points = get_initial_points(target, maincolor=maincolor, secondarycolor=secondarycolor) 
                            pygame.time.delay(1000)

    
    # Display text and triangles captured
    font = pygame.font.Font(None, 36)
    count_text = font.render(f"{count}", True, (255, 255, 255))
    instruction_text = font.render("Click Joystick to Collect Triangles", True, (255, 255, 255)) 
    draw_complete(target, secondarycolor, count)
    screen.blit(count_text, (10, 10))
    screen.blit(instruction_text, ((width/2)-200, height-30))

    pygame.display.update()
    clock.tick(FPS)
