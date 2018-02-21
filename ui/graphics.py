import string
import pygame
import time
from ui.menu import Menu

class GraphicsUI():
    
    def  __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 500))
        self.menu = Menu()

    def showIntro(self):
        img = pygame.image.load('ui/img/intro.png')
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(0.2)
        
    def showMainMenu(self, availableLevelIds: list) -> int:

        self.menu.show(availableLevelIds)
        return self.menu.waitForInput()
        
