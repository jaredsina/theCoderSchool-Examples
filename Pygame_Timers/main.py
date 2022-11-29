import pygame, sys

#initialize pygame
pygame.init()

#Game Items
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
black=(0,0,0)
white = (255,255,255)

#Two timer variables
current_time = 0
button_time = 0
color=black
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #event that sets off a two second timer
        if event.type == pygame.KEYDOWN:
            button_time=pygame.time.get_ticks()
            screen.fill(white)

    #get current time as game is going on
    current_time=pygame.time.get_ticks()

    #check if time has passed
    if current_time - button_time > 2000:
        screen.fill(black)
    pygame.display.flip()
    clock.tick(60)