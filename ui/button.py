import pygame 

class Button():


    def __init__(self, screen, name, x, y, show=True):
        
        if show:
            self.b = screen.blit( pygame.image.load("ui/img/" + name + ".png"), (x,y) )
            
        self.x = x
        self.y = y
        self.name = name
        self.screen = screen
        self.pressed = False

    def show(self):
        
        self.b = self.screen.blit( pygame.image.load("ui/img/" + self.name + ".png"), (self.x,self.y) )
        

    def setPressed(self, pos):
        
        if self.b.collidepoint(pos):
            
            self.pressed = True 
            
            self.b = self.screen.blit( pygame.image.load("ui/img/" + self.name + "_pressed.png"), (self.x,self.y) )
            pygame.display.flip()


    def isPressed(self):    
        
        if self.pressed:  
            
            self.b = self.screen.blit( pygame.image.load("ui/img/" + self.name + ".png"), (self.x,self.y) )
            pygame.display.flip()
            
            self.pressed = False
            
            return True 
             
        return False
    
    def getName(self):
        return self.name


class LevelButton (Button):
    
    def setLevel(self, level):
        self.level = level
        
    def getLevel(self):     
        return self.level