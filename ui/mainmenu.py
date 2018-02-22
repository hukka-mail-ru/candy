import pygame
import sys
import ui
import engine

class MainMenu():

    buttons = []

    def __init__(self, screen):
        self.screen = screen

    def show(self, levels: list):
        
        i = 0
        for level in levels:
            if (level.Available):
                b = ui.LevelButton(self.screen, 'level', 60*i, 150) 
                b.setLevel(level)     
                self.buttons.append(b)
                i += 1
        
        self.buttons.append(ui.Button(self.screen, 'retry', 50, 50))
        self.buttons.append(ui.Button(self.screen, 'exit', 200, 300))
        
        pygame.display.flip()


        while True:
            for event in pygame.event.get():
                                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                                                                            
                    for b in self.buttons:                        
                        b.setPressed(pygame.mouse.get_pos())
                            
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    for button in self.buttons:                    
                        if button.isPressed():                            
                            if button.getName() == "retry":
                                print("retry")
                            elif button.getName() == "exit":    
                                sys.exit()
                            elif button.getName() == "level":   
                                engine.GlobalGame.startLevel(button.getLevel())

# pragma: no cover
if __name__ == '__main__': # pragma: no cover

    
    w = MainMenu()
    w.show()
    w.waitForInput()