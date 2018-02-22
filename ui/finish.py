import pygame

import ui
import common

class Finish():

    buttons = []

    def __init__(self, screen):
        self.screen = screen


    def show(self, options):
        
        self.retryButton = ui.Button(self.screen, 'retry', 50, 50)
        self.mainmenuButton = ui.Button(self.screen, 'mainmenu', 100, 100)
        self.nextButton = ui.Button(self.screen, 'next', 200, 300)
        
            
        if(options == common.NEXT_LEVEL):        
            self.buttons.append(self.retryButton)
            self.buttons.append(self.mainmenuButton)
            self.buttons.append(self.nextButton)
            
        elif(options == common.RETRY):
            self.buttons.append(self.retryButton)
            self.buttons.append(self.mainmenuButton)       
            
        elif(options == common.MAIN_MENU):   
            self.buttons.append(self.mainmenuButton) 
        
        
        
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