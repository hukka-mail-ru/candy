import string
import pygame
import time

class GraphicsUI():
    
    def  __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 500))

    def showIntro(self):
        img = pygame.image.load('ui/intro.png')
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(1)
        
    def showMainMenu(self, availableLevelIds: list) -> int:
        pygame.draw.circle(self.screen, (255,255,255), (4, 4), 20) 
        pygame.display.flip()