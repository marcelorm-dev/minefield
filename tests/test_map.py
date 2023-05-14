import unittest
from src.core.map import Map



class MapTest(unittest.TestCase):
    
    def test_map_initialization(self):
        map = Map(5 , 5 , 5, [7, 11, 14, 20, 25])
        result = map.content(True)

        self.assertEqual(result, " 1  1  1  0  0 \n 2  *  2  1  1 \n *  2  2  *  2 \n 1  1  1  3  * \n 0  0  0  2  * \n")

    def test_map_with_invalid_rows_columns(self):
        try:
            map = Map(0, 5, 5)
        except Exception as err:
            self.assertEqual(str(err), 'Rows or columns can not be zero or negative.')
        
        try:
            map = Map(5, 0, 5)
        except Exception as err:
            self.assertEqual(str(err), 'Rows or columns can not be zero or negative.')
            return
        
        self.assertTrue(False, "It was supposed to never reach this line")


    def test_map_with_invalid_number_of_bombs(self):
        try:
            map = Map(5, 5, 0)
        except Exception as err:
            self.assertEqual(str(err), 'Number of bombs must be a number between 0 and 25.')
        
        try:
            map = Map(5, 5, 30)
        except Exception as err:
            self.assertEqual(str(err), 'Number of bombs must be a number between 0 and 25.')
            return
        
        self.assertTrue(False, "It was supposed to never reach this line")

    def test_map_with_max_number_of_bombs(self):
        map = Map(5, 5, 25)
        result = map.content(True)

        self.assertEqual(result, " *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  * \n")