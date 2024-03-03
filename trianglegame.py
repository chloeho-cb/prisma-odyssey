import pygame
import random
import numpy as np
import math

pygame.init()
run=True

#screensize
screensize = (width,height)=(pygame.display.Info().current_w,pygame.display.Info().current_h-120)#(1000,1000)
center=(int(width/2),int(height/2))
screen = pygame.display.set_mode(screensize)

#delta mov
ds=10
do=0.01

reds = [(255, 0, 0), (200, 0, 0), (150, 0, 0)]
oranges = [(255, 165, 0), (200, 130, 0), (150, 97, 0), (100, 65, 0), (50, 32, 0)]
yellows = [(255, 255, 0), (200, 200, 0), (150, 150, 0), (100, 100, 0), (50, 50, 0)]
greens = [(0, 255, 0), (0, 200, 0), (0, 150, 0), (0, 100, 0), (0, 50, 0)]
blues = [(0, 0, 255), (0, 0, 200), (0, 0, 150), (0, 0, 100), (0, 0, 50)]
purples = [(255, 0, 255), (200, 0, 200), (150, 0, 150), (100, 0, 100), (50, 0, 50)]
colors = [reds, oranges, yellows, greens, blues, purples]

maincolor = greens
secondarycolor = blues

# Function to divide a square into n triangles
def draw_complete(target, colors, n):
    angle = 360 / target
    x0, y0 = 70, 70
    side_length = 200 // 2 - 50
    
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
        pygame.draw.lines(screen, (255, 255, 255), True, [(x0, y0), (x1, y1), (x2, y2)], 4)

def get_initial_points(target, maincolor=greens, secondarycolor=blues):
    points = []
    for i in range(2000):
        n1 = random.randrange(-10000, 10000)
        n2 = random.randrange(-10000, 10000)
        n3 = random.randrange(-10000, 10000)
        rand = random.randrange(10, 700)
        points.append([n1, n2, n3, rand, random.choice(maincolor)])

    for i in range(target):
        n1 = random.randrange(0, 2000)  
        n2 = 0 
        n3 = random.randrange(0, 5000)  
        rand = random.randrange(10, 500)
        points.append([n1, n2, n3, rand, random.choice(secondarycolor)])
    
    return points

target = 3
points = get_initial_points(target)
count = 0
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    ################## keys
    keys=pygame.key.get_pressed()

    if keys[pygame.K_w]:
        for p in points:
            p[2]-=ds
    if keys[pygame.K_s]:
        for p in points:
            p[2] += ds

    if keys[pygame.K_a] or keys[pygame.K_d]:
        if keys[pygame.K_a]:
            for p in points:
                p[0], p[2] = np.cos(-do) * p[0] - np.sin(-do) * p[2], np.sin(-do) * p[0] + np.cos(-do) * p[2]
        else:
            for p in points:
                p[0], p[2] = np.cos(do) * p[0] - np.sin(do) * p[2], np.sin(do) * p[0] + np.cos(do) * p[2]


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
                pygame.draw.polygon(screen, p[4], rotated_vertices)  # Use p[4] as the color parameter
                if p[4] in secondarycolor:
                    triangle_area = abs((rotated_vertices[0][0] * (rotated_vertices[1][1] - rotated_vertices[2][1]) +
                                        rotated_vertices[1][0] * (rotated_vertices[2][1] - rotated_vertices[0][1]) +
                                        rotated_vertices[2][0] * (rotated_vertices[0][1] - rotated_vertices[1][1])) / 2)
                    screen_area = screensize[0] * screensize[1]
                    if triangle_area > screen_area * 0.1: # detect collision
                        count += 1 # increment count of found triangles
                        if p in points:
                            points.remove(p)
                        if count == target: # reset the game
                            target += 1
                            maincolor = secondarycolor
                            choices = colors.copy()
                            choices.remove(maincolor)
                            secondarycolor = random.choice(choices)
                            points = get_initial_points(target, maincolor=maincolor, secondarycolor=secondarycolor) 
                            count = 0

    
    # Display the count of red points
    font = pygame.font.Font(None, 36)
    text = font.render(f"{count}", True, (255, 255, 255))
    draw_complete(target, secondarycolor, count)
    screen.blit(text, (10, 10))

    pygame.display.update()
