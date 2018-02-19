import sqlite3
from engine.level import Level

class DB():
    
    
    def __init__(self):
        self.conn = sqlite3.connect('engine/candy.sqlite')
                
    
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
        
        nextLevelId = 0
        c.execute("SELECT COUNT(*) FROM levels WHERE Id = ?", (level.Id + 1,))        
        if c.fetchone() == (1,):
        
            c.execute("SELECT Id FROM levels WHERE Id = ?", (level.Id + 1,))
        
            nextLevelId = c.fetchone()[0]
                   

        c.execute("UPDATE levels SET available = 1 WHERE Id = ?", (level.Id + 1,))   
        
        self.conn.commit()
        
        return nextLevelId
    
    
    def isHighScore(self, level: Level, score: int) -> bool:
    
        c = self.conn.cursor()
        
        c.execute("SELECT HighScore FROM levels WHERE Id = ?", (level.Id,))
        
        highScore = int(c.fetchone()[0])
        
        if score > highScore:
            
            c.execute("UPDATE levels SET HighScore = ? WHERE Id = ?", (int(score), level.Id,))           
            self.conn.commit()            
            return True
        
        else:
            return False
            