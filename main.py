import pygame 
from sys import exit

#Classes

##letters
class Letter(pygame.sprite.Sprite()):
    def __init__(self, letter):
        super().__init__
        pass
        
#Functions

##Score function


#PyGame init
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Letter Strike")
clock = pygame.time.Clock()

game_active = False

#Game background
background_surf = pygame.image.load(r'D:\Programowanie\EgzaminyZeroToJunior\Letter Strike\graphics\background_game.jpg')

#Menu background


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        
            
    if game_active:
        screen.blit(background_surf, (0,0))
    else:
        #Gdy game over i start gry
        screen.fill('#c9934d')
        
        
        
        
    pygame.display.update()
    clock.tick(60)
        
            
            