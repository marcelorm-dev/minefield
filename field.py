class Field:
    
    def __init__(self, pos_x, pos_y, has_bomb) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bomb_counter = 0
        self.has_bomb = has_bomb

    def getPosX(self):
        return self.pos_x
    
    def __str__(self):
        #return f'[{self.pos_x}, {self.pos_y}]'
        if self.has_bomb:
            return ' B '
        else:
            return f' {self.bomb_counter} '
        
    def incrementBombCounter(self):
        self.bomb_counter += 1

#    def getPosY(self):
#        return self.pos_y
    
    def hasBomb(self):
        return self.has_bomb
    
#    def getBombCounter(self):
#        return self.bomb_counter
    
#    def addBombCounter(self):
#        self.bomb_counter += 1
#        return self.bomb_counter