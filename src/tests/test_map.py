import unittest
from src.core.map import Map


class MapTest(unittest.TestCase):
    
    def test_map_initialization(self):
        map = Map(5 , 5 , 5, [7, 11, 14, 20, 25])
        result = map.content(True)

        self.assertEqual(result, " 1  1  1  0  0 \n 2  *  2  1  1 \n *  2  2  *  2 \n 1  1  1  3  * \n 0  0  0  2  * \n")