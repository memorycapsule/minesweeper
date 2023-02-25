from tkinter import *
import settings
from cells import Cell
# Create the window
window = Tk()
window.title("Minesweeper")
window.geometry(f'{settings.window_width}x{settings.window_height}')
window.configure(background="#4a752c")

# Create the menu
menu_bar = Frame(window, bg="#4a752c", width=settings.window_width,
                 height=(settings.window_height/10))  # Take up only 15% of height
menu_bar.place(x=0, y=0)
menu_button = Button(menu_bar, text="Restart", bg="white", fg="black")
menu_button.place(x=settings.window_width*0.5, y=5)
# Create the game board
game_board = Frame(window, width=settings.window_width,
                   height=settings.window_height)
game_board.place(x=settings.window_width*0.2, y=settings.window_height * 0.05)

for i in range(settings.grid_size):
    for j in range(14):
        c = Cell(i, j)
        c.create(game_board)
        c.cell_btn.grid(row=i, column=j)


Cell.place_mines()
print(Cell.grid)
window.mainloop()
