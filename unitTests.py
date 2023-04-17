import unittest
from cell import Cell

class CellTest(unittest.TestCase):

    def test_update_state(self):
        # Test cases for update_state() method
        # Create Cell instances with different initial states
        cell1 = Cell(True) # alive cell
        cell2 = Cell(False) # dead cell

        # Test for alive cell with fewer than two live neighbors
        cell1.update_state(1)
        self.assertFalse(cell1.is_alive()) # expected output: False

        # Test for alive cell with two live neighbors
        cell1.update_state(2)
        self.assertTrue(cell1.is_alive()) # expected output: True

        # Test for alive cell with three live neighbors
        cell1.update_state(3)
        self.assertTrue(cell1.is_alive()) # expected output: True

        # Test for alive cell with more than three live neighbors
        cell1.update_state(4)
        self.assertFalse(cell1.is_alive()) # expected output: False

        # Test for dead cell with exactly three live neighbors
        cell2.update_state(3)
        self.assertTrue(cell2.is_alive()) # expected output: True

    def test_get_neighboring_cells(self, world):
        # Test cases for get_neighboring_cells() method
        # Create Cell instances at different positions in the grid
        cell1 = Cell(True, 0, 0) # top-left corner
        cell2 = Cell(True, 0, 1) # top row, second column
        cell3 = Cell(True, 1, 0) # second row, first column

        # Test for neighboring cells of cell1
        neighboring_cells1 = cell1.get_neighboring_cells(world)
        self.assertEqual(len(neighboring_cells1), 3) # expected output: 3

        # Test for neighboring cells of cell2
        neighboring_cells2 = cell2.get_neighboring_cells(world)
        self.assertEqual(len(neighboring_cells2), 5) # expected output: 5

        # Test for neighboring cells of cell3
        neighboring_cells3 = cell3.get_neighboring_cells(world)
        self.assertEqual(len(neighboring_cells3), 5) # expected output: 5

if __name__ == '__main__':
    unittest.main()
