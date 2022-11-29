import pygame

pygame.init()

screen= pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame Animations')

class Tilesheet:
    def __init__(self,filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self,rectangle):

        #create a rect out of the frame chosen
        rect = pygame.Rect(rectangle)

        #create a surface to blit image onto
        image = pygame.Surface(rect.size).convert_alpha()

        #blit specifiic image from sheet onto the image
        image.blit(self.sheet,(0,0),rect)
        image=pygame.transform.scale(image,(200,150))
        return image

#Game Variables


#Animation Timer Variables
last_update = pygame.time.get_ticks()
current_time=0
frame_timer = 250
frame =0

#Sprite dimension 50x37px
player_sheet = Tilesheet('./src/adventurer-Sheet.png')
#Rect is (x,y x+offset,y+offset)
frame1 = pygame.Rect(0,0,50,37)
frame2 = pygame.Rect(50,0,50,37)
frame3 = pygame.Rect(100,0,50,37)
frame4 = pygame.Rect(150,0,50,37)
frame1 = player_sheet.image_at(frame1)
frame2 = player_sheet.image_at(frame2)
frame3 = player_sheet.image_at(frame3)
frame4 = player_sheet.image_at(frame4)

#Create Animation List
idle_animation=[frame1,frame2,frame3,frame4]

clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill('white')
    current_time=pygame.time.get_ticks()
    if current_time-last_update>=1:
        screen.blit(idle_animation[frame],(0,0))
        frame+=1
        last_update=pygame.time.get_ticks()
        if frame>3:
            frame=0
    pygame.display.update()
    clock.tick(8)