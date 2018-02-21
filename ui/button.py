import pygame 

class Button():


    def __init__(self, screen, file, x, y):
        
        self.b = screen.blit( pygame.image.load("ui/img/" + file + ".png"), (x,y) )
        self.x = x
        self.y = y
        self.file = file
        self.screen = screen
        self.pressed = False

    def setPressed(self, pos):
        
        if self.b.collidepoint(pos):
            
            self.pressed = True 
            
            self.b = self.screen.blit( pygame.image.load("ui/img/" + self.file + "_pressed.png"), (self.x,self.y) )
            pygame.display.flip()


    def isPressed(self):    
        
        if self.pressed:  
            
            self.b = self.screen.blit( pygame.image.load("ui/img/" + self.file + ".png"), (self.x,self.y) )
            pygame.display.flip()
            
            self.pressed = False
            
            return True 
             
        return False


class LevelButton (Button):
    
    def setLevel(self, level):
        self.level = level
        
    def getLevel(self):     
        return self.level