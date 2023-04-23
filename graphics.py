#functions related to the visualization and grapjical represntation of the game of life

import tkinter as tk
from world import World
from typing import Union

class Graphics(tk.Tk):
    def __init__(self, row: int, col: int, cell_size: int):
        super().__init__()

        # Set up the main window
        self.title("Game of Life")
        self.geometry("800x800")

        self.row = row
        self.col = col
        self.cell_size = cell_size
        self.world = World(row, col)
        self.world.randomize_grid()

        self.canvas = tk.Canvas(self, width=col*cell_size, height=row*cell_size, bg='white')
        self.canvas.pack()

        self.start_button = tk.Button(self, text="Start", command=self.start_simulation)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_simulation)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side="left")

        self.canvas.bind("<Button-1>", self.toggle_cell_state)

        self.is_running = False

        self.load_button = tk.Button(self, text="Load", command=self.load_pattern)
        self.load_button.pack(side="left")

        self.save_button = tk.Button(self, text="Save", command=self.save_pattern)
        self.save_button.pack(side="left")

        # Add scale widget for adjusting simulation speed

        self.speed_scale = tk.Scale(self, from_=10, to=1000, orient="horizontal", label="Speed")
        self.speed_scale.set(100)
        self.speed_scale.pack(side="left")
    
    def start_simulation(self) -> None:
        # Start the simulation by setting the is_running flag and updating the world
        if not self.is_running:
            self.is_running = True
            self.update_world()

    def stop_simulation(self) -> None:
        # Stop the simulation by clearing the is_running flag
        self.is_running = False

    def reset_simulation(self) -> None:
        # Reset the simulation by stopping it, randomizing the grid, and redrawing the world
        self.stop_simulation()
        self.world.randomize_grid()
        self.draw_world()


    def update_world(self) -> None:
        # Update the world using the World class methods and redraw the world
        self.world.update_world()
        self.draw_world()
        self.after(100, self.update_world)  # Update the world every 100ms, adjust the delay as needed
        self.after(self.speed_scale.get(), self.update_world)

    def draw_world(self) -> None:
        # Draw the current state of the world on the canvas using rectangles for alive cells
        self.canvas.delete("all")
        for i in range(self.row):
            for j in range(self.col):
                if self.world.grid[i][j].alive:
                    x1, y1 = j * self.cell_size, i * self.cell_size
                    x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")

    def toggle_cell_state(self, event: Union[tk.Event, tk.MouseEvent]) -> None:
        # Toggle the state of the cell that was clicked by the user
        i = event.y // self.cell_size
        j = event.x // self.cell_size
        self.world.grid[i][j].alive = not self.world.grid[i][j].alive
        self.draw_world()

    def save_pattern(self):
        pattern_name = input("Enter a name for the pattern: ")
        self.world.save_pattern(pattern_name)

    def load_pattern(self):
        pattern_name = input("Enter the name of the pattern to load: ")
        self.world.load_pattern(pattern_name)

