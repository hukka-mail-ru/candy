
#import pygame

class Window():
    
    def __init__(self, x, y, w, h):
        
    button = pygame.image.load('Pictures/cards/stand.png').convert_alpha()
    screen.blit(button,(300,200))
    pygame.display.flip()

    ## does button need to be 'pygame.sprite.Sprite for this? ##
    ## I use 'get_rect() ##
    button = button.get_rect()        

if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    
    if b.collidepoint(pos):
 # pragma: no cover
if __name__ == '__main__': # pragma: no cover
    pygame.init()
    self.screen = pygame.display.set_mode((480, 500))
    
    '''https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect''
    