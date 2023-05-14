import random
from src.core.field import Field
from src.core.matriz import Matriz

class Map:

    def __init__(self, rows:int, columns:int, num_of_bombs:int, bomb_positions:list[int]=[]):
        if rows <= 0 or columns <= 0:
            raise Exception('Rows or columns can not be zero or negative.')

        if num_of_bombs <= 0  or num_of_bombs > (rows * columns):
            raise Exception(f'Number of bombs must be a number between 0 and {rows * columns}.')       
        
        self._rows = rows
        self._columns = columns
        self._matrix = Matriz[Field](rows, columns)

        self._bomb_positions = self._calculate_bomb_positions(num_of_bombs, bomb_positions)

        self._initialize_fields()
        self._count_bombs_around_fields()

    def _calculate_bomb_positions(self, num_of_bombs, bomb_positions):
        if len(bomb_positions) == 0:
            random.seed()
            return random.sample(range(1, (self._rows * self._columns) + 1), k=num_of_bombs)
        else:
            return bomb_positions

    def _initialize_fields(self):
        for row in range(self._rows):
            for column in range(self._columns):
                field_position = (row * self._columns) + (column + 1)
                self._matrix.append(Field(row, column, field_position in self._bomb_positions))

    def _count_bombs_around_fields(self):
        for field in self._matrix.elements():
            for neighboor in self._matrix.neighboors(field.get_pos_x(), field.get_pos_y()):
                if neighboor.has_bomb():
                    field.increment_bomb_counter()

    def content(self, force_show_content=False) -> str:
        content = ''

        for row in range(self._rows):
            for field in self._matrix.elements_of_row(row):
                if force_show_content:
                    field.show_content()
                content = content + str(field)  
            content = content + '\n'
        
        return content

 
    def show_content_in(self, row:int, column:int):
        field = self._matrix.element(row, column)
        
        if not field.is_hidden_content():
            return False
        
        field.show_content()

        if field.has_bomb():    
            return True
        
        if field.get_bomb_counter() > 0:
            return False
        
        for neighboor_field in self._matrix.neighboors(field.get_pos_x(), field.get_pos_y()):
            self.show_content_in(neighboor_field.get_pos_x(), neighboor_field.get_pos_y())

        return False