import pygame
import sys
from ui.button import Button  
from ui.button import LevelButton 

class MainMenu():

    levelButtons = []
    buttons = []


    def show(self, availableLevelIds):
        pygame.init()
        screen = pygame.display.set_mode((480, 500))
        
        i = 0
        for availableLevelId in availableLevelIds:
            b = LevelButton(screen, 'level', 60*i, 150) 
            b.setLevel(availableLevelId)     
            self.levelButtons.append(b)
            self.buttons.append(b)
            i += 1
        
        self.retryButton = Button(screen, 'retry', 50, 50)
        self.exitButton = Button(screen, 'exit', 200, 300)
        self.buttons.append(self.retryButton)
        self.buttons.append(self.exitButton)
        
        pygame.display.flip()

  

    def waitForInput(self) -> int:
    
        while True:
            for event in pygame.event.get():
                                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                                                                            
                    for b in self.buttons:                        
                        b.setPressed(pygame.mouse.get_pos())
                            
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    if self.retryButton.isPressed():
                        print("retry")
                        
                    if self.exitButton.isPressed():
                        sys.exit()

                    for levelButton in self.levelButtons:                        
                        if levelButton.isPressed():
                            return levelButton.getLevel()

 # pragma: no cover
if __name__ == '__main__': # pragma: no cover

    
    w = MainMenu()
    w.show()
    w.waitForInput()


   