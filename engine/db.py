import sqlite3

class DB():
    
    
    def __init__(self):
        self.conn = sqlite3.connect('engine/candy.sqlite')
        print ("connected")
                
    
    def getAvailableLevels(self) -> list:
        
        c = self.conn.cursor()
        
        c.execute("SELECT Id, Name FROM levels WHERE available > 0")
        
        return c.fetchall()


    def openNextLevel(self, level: int):
                                 
        c = self.conn.cursor()
        
        c.execute("UPDATE levels SET available = 1 WHERE Id = ?", (level + 1,))   
        
        self.conn.commit()