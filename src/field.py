class Field:
    
    def __init__(self, pos_x:int, pos_y:int, has_bomb:bool):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._bomb_counter = 0
        self._has_bomb = has_bomb
        self._is_hidden_content = True

    def get_pos_x(self):
        return self._pos_x
    
    def get_pos_y(self):
        return self._pos_y

    def get_bomb_counter(self):
        return self._bomb_counter

    def has_bomb(self):
        return self._has_bomb
    
    def is_hidden_content(self):
        return self._is_hidden_content
    
    def show_content(self):
        self._is_hidden_content = False
    
    def __str__(self):
        if self.is_hidden_content():
            return ' ■ '
        elif self._has_bomb:
            return ' * '
        else:
            return f' {self._bomb_counter} '
        
    def increment_bomb_counter(self):
        if not self.has_bomb():
            self._bomb_counter += 1
    