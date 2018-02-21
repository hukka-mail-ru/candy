import string
import pygame
import time
import engine
import ui.mainmenu

class GraphicsUI():
    
    def  __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 500))
        self.mainMenu = ui.mainmenu.MainMenu()

    def showIntro(self):
        img = pygame.image.load('ui/img/intro.png')
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(0.2)
        
    def showMainMenu(self, levels: list) -> engine.Level:

        self.mainMenu.show(levels)
        return self.mainMenu.waitForInput()
        
