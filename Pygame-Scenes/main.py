from json import load
import pygame, sys

#initialize pygame
pygame.init()

#Create a player object
class Player():
    def __init__(self,filename,width,height):
        image = pygame.image.load(filename)
        self.surface = pygame.Surface((width,height)).convert_alpha()
        self.surface.blit(image,(50,50),(0,0,width,height))
    def draw(self):
        screen.blit(self.surface,(100,100))

#Create a button object
class Button():

    def __init__(self,filename,width,height):
        image = pygame.image.load(filename).convert_alpha()
        self.surface = pygame.Surface((width,height)).convert_alpha()
        self.surface.blit(image,(50,50),(0,0,width,height))
    
    def draw(self):
        screen.blit(self.surface,(0,0))

#Game State class is used to create a game 
class GameState():

    #By Default start on the intro scene
    def __init__(self):
        self.state = "intro"

    #State manager method is used to control which scene is being drawn on the screen in the game loop
    def state_manager(self):
        if self.state == 'main_game':
            self.main_game()
        elif self.state == 'intro':
            self.intro()
   
   #Intro scene method
    def intro(self):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    self.state='main_game'
            screen.blit(background, (0,0))
            load_button.draw()
            pygame.display.flip()

    #Main Game Scene method
    def main_game(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

     #Draw scene on display
        screen.fill(black)
        screen.blit(background, (0,0))
        player.draw()
        pygame.display.flip()

#Game Objects
size =width,height = 1000,500
black =0,0,0
screen = pygame.display.set_mode(size)
player= Player('./assets/sprites/characters/player.png',100,100)
background = pygame.image.load('./assets/sprites/characters/slime.png')
load_button = Button('./assets/load_button2.png',920,360)
game_state = GameState()
clock=pygame.time.Clock()

#Game Loop
while True:
    game_state.state_manager()
    clock.tick(60)
