import pygame
import random
import numpy as np

pygame.init()
run=True

#screensize
screensize = (width,height)=(1000,1000)
center=(int(width/2),int(height/2))
screen = pygame.display.set_mode(screensize)

#delta mov
ds=10
do=0.01

greens = [(0, 255, 0), (0, 200, 0), (0, 150, 0), (0, 100, 0), (0, 50, 0)]
reds = [(255, 0, 0), (200, 0, 0), (150, 0, 0)]

#Stars
points=[]
for i in range(3000):
    n1 = random.randrange(-10000,10000)
    n2 = random.randrange(-10000,10000)
    n3 = random.randrange(-10000,10000)
    rand = random.randrange(10,500)
    points.append([n1,n2,n3,rand,greens[random.randrange(0,5)]])

# Add 3 red points
for i in range(3):
    n1 = random.randrange(0, 2000)  
    n2 = 0 
    n3 = random.randrange(0, 5000)  
    rand = random.randrange(10, 500)
    points.append([n1, n2, n3, rand, reds[i]])
    print(n1, n2, n3, rand, reds[i])

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
            p[0], p[1], p[2] = random.randrange(-10000,10000), random.randrange(-10000,10000), 10000
            p[3] = random.randrange(10,500)
            p[4] = greens[random.randrange(0,5)]
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
                if p[4] in reds:
                    triangle_area = abs((rotated_vertices[0][0] * (rotated_vertices[1][1] - rotated_vertices[2][1]) +
                                        rotated_vertices[1][0] * (rotated_vertices[2][1] - rotated_vertices[0][1]) +
                                        rotated_vertices[2][0] * (rotated_vertices[0][1] - rotated_vertices[1][1])) / 2)
                    screen_area = screensize[0] * screensize[1]
                    if triangle_area > screen_area * 0.5:
                        count += 1
                        points.remove(p)

    
    # Display the count of red points
    font = pygame.font.Font(None, 36)
    text = font.render(f"Red points: {count}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
