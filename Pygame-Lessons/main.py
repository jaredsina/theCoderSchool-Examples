import pygame
import random
intro = True
gameDisplay = pygame.display.set_mode((720,720))


# Initializing Pygame
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((400,400))
  
# Initialing Color
randomNumber = random.randrange(1,4)
red = (255,0,0)
color2 = (0,255,0) 
color3=(0,0,255)
color=(255,255,255)

# Drawing Rectangle

def colorPicker():
    global color
    if randomNumber==1:
        color=red
    elif randomNumber==2:
        color=color2
    

while intro:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(surface, color, pygame.Rect(125, 30, 100, 100))

    pygame.draw.rect(surface, red, pygame.Rect(150, 150, 50, 50))
    pygame.draw.rect(surface, color2, pygame.Rect(0, 150, 50, 50))
    pygame.draw.rect(surface, color3, pygame.Rect(300, 150, 50, 50))

    pygame.display.flip()   

            