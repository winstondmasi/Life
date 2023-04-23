from graphics import Graphics

def main():
    row = 50
    col = 50
    cell_size = 10

    app = Graphics(row, col, cell_size)
    app.mainloop()

if __name__ == "__main__":
    main()
