# Life

This is a Python implementation of Conway's Game of Life using the Tkinter library for the graphical user interface.

## Overview

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

The game consists of a grid of cells, which can be in one of two states: alive or dead. Each cell interacts with its eight neighboring cells according to a set of simple rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Features

- Start, stop, and reset the simulation with dedicated buttons
- Manually toggle the state of individual cells by clicking on them
- Save and load custom patterns for reuse
- Adjust the simulation speed with a slider
- User-friendly graphical interface using Tkinter

## Usage

To run the game, execute the following command:

```bash
python main.py
```

The graphical user interface allows you to start, stop, and reset the simulation. You can also manually toggle the state of individual cells by clicking on them. Additionally, you can save and load custom patterns.

## Files

- main.py: The main script to run the Game of Life.
- world.py: The World class representing the Game of Life grid and implementing the rules of the game.
- cell.py: The Cell class representing a single cell in the Game of Life grid.
- graphics.py: The Graphics class implementing the Tkinter-based graphical user interface.

## Future functionality

- Resizable grid
- Import/export patterns
- Pattern library
- Custom rules
- Record and playback
