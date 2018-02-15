

class Game():
    
    def chooseWord(self):
        
        return "Hello"
    
    
    def start(self):
        
        secretWord = self.chooseWord()
        
        print("chosen word", secretWord)
        
        guessed = input('input something!: ') 
        
        print("guessed", guessed)
        
        if (secretWord == guessed):
            print("YES!")
        else:
            print("NO!")

if __name__ == '__main__': # pragma: no cover
    game = Game()
    game.start()    