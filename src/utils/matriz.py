from typing import TypeVar, Generic

T = TypeVar('T')

class Matriz(Generic[T]):

    def __init__(self, rows:int, columns:int):
        self._rows = rows
        self._columns = columns
        self._list:list[T] = []

    def append(self, obj):
        if (len(self._list) == self._rows * self._columns):
            raise Exception(f"Appending more elements than allowed. It's allowed {self._rows * self._columns} elements.")
        self._list.append(obj)

    def elements(self) -> list[T]:
        return self._list.copy()

    def element(self, x:int, y:int) -> T:
        return self._list[(x * self._columns) + y]
    
    def elements_of_row(self, x:int) -> list[T]:
        elements:list[T] = []

        for y in range(self._columns):
            elements.append(self.element(x, y))

        return elements
    
    def neighboors(self, x:int, y:int) -> list[T]:
        neighboors:list[T] = []

        for index in [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]:
            if (x + index[0] in range(self._rows) and  y + index[1] in range(self._columns)):
                element  = self.element(x + index[0], y + index[1])
                #if element:
                neighboors.append(element)

        return neighboors
    
    def length(self):
        return self._rows * self._columns

    def __str__(self) -> str:
        text = "["

        for element in self._list:
            text = text + str(element)
            if ((self._list.index(element) + 1) % self._columns == 0):
                if (self._list.index(element) != len(self._list) - 1):
                    text = text + '\n'
            else:
                text = text + ','


        text = text + ']'
        
        return text