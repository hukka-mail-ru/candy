


class Level():
    
    Id = 0
    Name = "" 
    Available = 0
    MinCipherLen = 0
    MaxCipherLev = 0
    MinWordLen = 0
    MaxWordLen = 0
    HighScore = 0
    
    def __init__(self, level: tuple):
        (self.Id, self.Name, self.Available, self.MinCipherLen, 
         self.MaxCipherLen, self.MaxCipherVal, self.MinWordLen, 
         self.MaxWordLen, self.HighScore) = level
     
