from src.map import Map

class GameController:

    def __init__(self, map:Map):
        self._is_game_over = False
        self._map = map

    def is_game_over(self): 
        return self._is_game_over

    def click_on(self, row, column):
        self._is_game_over = self._map.show_content_in(row, column)
        return self._is_game_over
    
    def map_content(self):
        return self._map.content()
    


