import unittest 
from src.core.matriz import Matriz

class MatrizUnitTest(unittest.TestCase):

    def test_matriz_length(self):
        matriz = Matriz(3,3)
        self.assertEqual(matriz.length(), 9)

    def test_append_nine_numbers(self):
        matriz = Matriz(3,3)

        for i in range(1,10):
            matriz.append(i)

        self.assertEqual(matriz.elements(), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(str(matriz), "[1,2,3\n4,5,6\n7,8,9]")


    def test_elements_of_row(self):
        matriz = Matriz(3,3)

        for i in range(1,10):
            matriz.append(i)

        self.assertEqual(matriz.elements_of_row(0), [1,2,3])
        self.assertEqual(matriz.elements_of_row(1), [4,5,6])
        self.assertEqual(matriz.elements_of_row(2), [7,8,9])

    def test_append_more_elements_than_allowed(self):
        matriz = Matriz(3,3)

        try:
            for i in range(1,11):
                matriz.append(i)
        except Exception as err:
            self.assertIsInstance(err, Exception)
            return
        
        self.assertTrue(False, "It was supposed to never reach this line")

    def test_get_element_by_indexes(self):
        matriz = Matriz(3,3)

        for i in range(1,10):
            matriz.append(i)

        self.assertEqual(matriz.element(0,1), 2)
        self.assertEqual(matriz.element(1,1), 5)
        self.assertEqual(matriz.element(2,1), 8)

    def test_neighboors_elements(self):
        matriz = Matriz(3,3)

        for i in range(1,10):
            matriz.append(i)

        self.assertEqual(matriz.neighboors(0,0), [2,4,5])
        self.assertEqual(matriz.neighboors(0,1), [1,3,4,5,6])
        self.assertEqual(matriz.neighboors(1,0), [1,2,5,7,8])
        self.assertEqual(matriz.neighboors(1,1), [1,2,3,4,6,7,8,9])
        self.assertEqual(matriz.neighboors(2,1), [4,5,6,7,9])
        self.assertEqual(matriz.neighboors(2,2), [5,6,8])