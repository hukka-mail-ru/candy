import pygame

import ui
import common

class Finish():

    buttons = []

    def __init__(self, screen):
        self.screen = screen


    def show(self, options):
        
        retryButton = ui.Button(self.screen, 'retry', 50, 50, False)
        mainmenuButton = ui.Button(self.screen, 'mainmenu', 100, 100, False)
        nextButton = ui.Button(self.screen, 'next', 200, 300, False)
                    
        if(options == common.NEXT_LEVEL):        
            self.buttons.append(retryButton)
            self.buttons.append(mainmenuButton)
            self.buttons.append(nextButton)
            
        elif(options == common.RETRY):
            self.buttons.append(retryButton)
            self.buttons.append(mainmenuButton)       
            
        elif(options == common.MAIN_MENU):   
            self.buttons.append(mainmenuButton) 

        for button in self.buttons:
            button.show()
        
        
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
                                return common.RETRY
                            
                            elif button.getName() == "mainmenu":
                                print("main menu")
                                return common.MAIN_MENU
                            
                            elif button.getName() == "next":
                                print("nextLevel")
                                return common.NEXT_LEVEL