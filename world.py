#function that represents the entire game world
import random
from typing import List
from cell import Cell

class World:
    """Represents the Game of Life world."""

    def __init__(self, row: int, col: int):
        #Initializes the World with rows and columns
        self.row = row
        self.col = col
        self.grid: List[List[Cell]] = [[Cell(False, i, j) for j in range(col)] for i in range(row)]
        self.randomize_grid()

    #Randomizes the grid based on the given probability
    def randomize_grid(self, probability_alive: float = 0.5) -> None:
        for i in range(self.row):
            for j in range(self.col):
                self.grid[i][j].alive = random.random() < probability_alive

    #Updates the world by applying the Game of Life rules.
    def update_world(self) -> None:
        new_grid: List[List[Cell]] = [[Cell(False, i, j) for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                cell = self.grid[i][j]
                alive_neighbours = self.get_alive_neighbours(i, j)
                new_state = self.get_new_state(cell.alive, alive_neighbours)
                new_grid[i][j].alive = new_state
        self.grid = new_grid

    #Counts alive neighbours for a given cell
    def get_alive_neighbours(self, row: int, col: int) -> int:
        alive_neighbours = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i, j) != (row, col) and 0 <= i < self.row and 0 <= j < self.col:
                    if self.grid[i][j].alive:
                        alive_neighbours += 1
        return alive_neighbours

    # Determines the new state for a cell based on its current state and alive neighbours
    def get_new_state(self, current_state: bool, alive_neighbours: int) -> bool:
        if current_state:
            return alive_neighbours == 2 or alive_neighbours == 3
        else:
            return alive_neighbours == 3