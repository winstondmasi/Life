#functions for single cells in the program 

class Cell:
    # attributes
    def __init__(self, state, row, col):
        self.state = state  # "alive" or "dead"
        self.row = row      # row index on the grid
        self.col = col      # colomn index on the grid

    # update the state of the cells based off of how many neighbours surrounding it
    def updsate_state(self, number_of_neighbours):
        neighbour_counter = 0

        for cell in number_of_neighbours:
            if cell.state == "alive":
                neighbour_counter += 1
        
        if self.state == "alive":
            if neighbour_counter < 2 or neighbour_counter > 3:
                self.state == "dead"
        else:
            if neighbour_counter == 3:
                self.state == "alive"

    # get neighbouring cells from the world and return it
    def get_neighbouring_cells(self, world):
        number_of_neighbours = []

        for i in range(self.row - 1, self.row + 2):
            for j in range(self.col - 1, self.col + 2):
                if(i, j) != (self.row, self.col) and 0 <= i < world.row and 0 <= j < world.col:
                    number_of_neighbours.append(world.grid[i][j])

        return number_of_neighbours
        

