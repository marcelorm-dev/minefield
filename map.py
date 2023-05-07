import random
from field import Field

class Map:

    def __init__(self, rows, columns, num_of_bombs) -> None:
        self.rows = rows
        self.columns = columns
        
        random.seed()
        self.bomb_positions = random.sample(range(rows*columns), k=num_of_bombs)
        print(f'Bombs: {self.bomb_positions}')

        self.fields = []

        field_counter = 1
        for row in range(self.rows):
            self.fields.append([])
            for column in range(columns):
                self.fields[row].append(Field(row, column, field_counter in self.bomb_positions))
                field_counter += 1

        for row in range(self.rows):
            for column in range(self.columns):
                avaliated_field = self.fields[row][column]

                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if row + i in range(self.rows) and column + j  in range(self.columns):
                            neighboor_field = self.fields[row + i][column + j]
                            if avaliated_field != neighboor_field and neighboor_field.hasBomb():
                                avaliated_field.incrementBombCounter() 

 
    def print(self):
        for row in range(self.rows):
            for field in self.fields[row]:
                print(field, end='')  
            print()
 