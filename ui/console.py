import string

class ConsoleUI():
    
    
    def showField(self, rulesDict, cipheredWord):

        print("Rules:")
        for letter in rulesDict:
            print("dict", letter, rulesDict[letter])
        print("\n")
    
        print("Guess this!")
        for cipheredLetter in cipheredWord:
            l = ""
            for num in cipheredLetter:
                l += str(num) + " "       
            print("ciphered", l)
    
    
    def inputUserGuess(self) -> string:
        guessed = input('\ninput something!: ')         
        print("guessed", guessed)
        return guessed
    
    def outputWin(self):
        print("You win!")
        
    def outputLoose(self):
        print("You loose!")