import sqlite3
from engine.level import Level

class DB():
    
    
    def __init__(self):
        self.conn = sqlite3.connect('engine/candy.sqlite')
        print ("connected")
                
    
    def getAvailableLevelIds(self) -> list:
        
        c = self.conn.cursor()
        
        c.execute("SELECT Id FROM levels WHERE available > 0")
        
        levelIds = []
        for row in c.fetchall():                
            (levelId, ) = row
            levelIds.append(levelId)
        
        return levelIds


    def getLevel(self, levelId: int) -> Level:
        
        c = self.conn.cursor()
        
        c.execute("SELECT * FROM levels WHERE Id = ?", (levelId,))
        
        return Level(c.fetchone())
    

    def openNextLevel(self, level: Level):
                                 
        c = self.conn.cursor()
        
        c.execute("UPDATE levels SET available = 1 WHERE Id = ?", (level.getId() + 1,))   
        
        self.conn.commit()