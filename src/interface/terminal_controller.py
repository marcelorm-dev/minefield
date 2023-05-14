import os
from src.core.game_controller import GameController
from src.core.map import Map

class TerminalController:

    def configure_game(self):
        map = Map(10, 10, 10)
        self._game = GameController(map)

    def run_game(self):
        self._show_map()
        self._click_on()

    def _show_map(self):
        os.system("clear")
        print(self._game.map_content())

    def _click_on(self):
        field_positions = self._field_positions()
        if len(field_positions) > 0:
            self._game.click_on(field_positions[0], field_positions[1])

    def _field_positions(self) -> list[int]:
        try:
            row = int(input("Digite o número da linha: ")) - 1
            column = int(input("Digite o número da coluna: ")) -1
            return [row, column]
        except:
            self._show_map()
            return []
    
    def is_game_over(self):
        return self._game.is_game_over()

    def end_game(self):
        self._show_map()
        print("Bummmmmm!!!!")
