


class Level():
    
    def __init__(self, level: tuple):
        (self.id, self.name, self.available, self.minCipherLevel, 
         self.maxCipherLevel, self.maxCipherVal, self.minWordLen, self.maxWordLen) = level
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getMinWordLen(self):
        return self.minWordLen
    
    def getMaxWordLen(self):
        return self.maxWordLen
    
    def getMinCipherLen(self):
        return self.minCipherLevel
    
    def getMaxCipherLen(self):
        return self.maxCipherLevel
    
    def getMaxCipherVal(self):
        return self.maxCipherVal