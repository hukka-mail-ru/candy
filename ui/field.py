import pygame
import pygame.locals as pl
import ui.pygame_textinput
import string

class Field():
    
    def __init__(self, screen):
        self.screen = screen
    
    def show(self, rulesDict, cipheredWord):
        
        self.screen.fill((0,0,0))
        
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render('Rules:', False, (255, 255, 0))
        self.screen.blit(textsurface,(50,50))
        
         
        y = 100 
        for letter in rulesDict:
            textsurface = myfont.render(letter, False, (255, 255, 0))
            self.screen.blit(textsurface,(50,y-20))
        
            
            x = 100
            for num in rulesDict[letter]:
                
                color = (255,215,0) # gold
                
                if num == 0: 
                    color = (204,102,51) # chocolate
                elif num == 1:
                    color = (238,130,238) # violet
                elif num == 2:
                    color = (255,235,205)  # blanched almond
                elif num == 3:
                    color = (135,206,235) # skyblue
                elif num == 4:
                    color = (255,127,80) #coral
                    
                pygame.draw.circle(self.screen, color, (x, y), 10)
                x += 30
                
            y+=30
        
        
        textsurface = myfont.render('Guess this:', False, (255, 255, 255))
        self.screen.blit(textsurface,(50,300))
        
        x = 50
        for cipheredLetter in cipheredWord:            
            for num in cipheredLetter:
                
                color = (255,215,0) # gold
                
                if num == 0: 
                    color = (204,102,51) # chocolate
                elif num == 1:
                    color = (238,130,238) # violet
                elif num == 2:
                    color = (255,235,205)  # blanched almond
                elif num == 3:
                    color = (135,206,235) # skyblue
                elif num == 4:
                    color = (255,127,80) #coral
                    
                pygame.draw.circle(self.screen, color, (x, 350), 10)
                x += 30
                                                                                    
                                                    
        pygame.display.flip()
        
        
    def inputUserGuess(self) -> string:   
        # Create TextInput-object
        textinput = ui.pygame_textinput.TextInput()
        
        clock = pygame.time.Clock()
        
        while True:
        
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pl.K_RETURN:
                    guessed = textinput.get_text()
                    return guessed
        
            # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            self.screen.blit(textinput.get_surface(), (10, 10))
        
            pygame.display.update()
            clock.tick(30)