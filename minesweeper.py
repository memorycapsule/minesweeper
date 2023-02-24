from tkinter import *
import settings
from cells import Cell
# Create the window
window = Tk()
window.title("Minesweeper")
window.geometry(f'{settings.window_width}x{settings.window_height}')
window.configure(background="grey")
window.resizable(False, False)

# Create the menu
menu_bar = Frame(window, bg="white", width=settings.window_width,
                 height=(settings.window_height/25))  # Take up only 15% of height
menu_bar.place(x=0, y=0)
menu_button = Button(menu_bar, text="Menu", bg="white", fg="black")
menu_button.place(x=settings.window_width*0.5, y=5)
# Create the game board
game_board = Frame(window, bg="grey", width=settings.window_width,
                   height=settings.window_height)
game_board.place(x=settings.window_width*0.3, y=settings.window_height * 0.15)

for i in range(settings.grid_size):
    for j in range(settings.grid_size):
        c = Cell(i, j)
        c.create(game_board)
        c.cell_btn.grid(row=i, column=j)

Cell.place_mines()
print(Cell.grid)
window.mainloop()
