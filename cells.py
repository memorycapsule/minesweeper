from tkinter import Button, PhotoImage
import random
import settings


class Cell:
    grid = []

    def __init__(self, x, y, is_mine=False, is_flagged=False):
        self.is_mine = is_mine
        self.is_flagged = is_flagged
        self.is_pressed = False
        self.x = x
        self.y = y
        self.cell_btn = None
        self.flag_img = PhotoImage(file=".\\resources\\flag.gif")
        self.mine_img = PhotoImage(file=".\\resources\\mine.gif")
        self.plain_img = PhotoImage(file=".\\resources\\plain.png")

        Cell.grid.append(self)

    def create(self, frame):
        button = Button(frame, bg="#aad751", text=str(
            " "), anchor="center", font=("Arial", 10, "bold"),
            fg="black", image=self.plain_img, width=30, height=30, bd=0, cursor="arrow")
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.flag)
        self.cell_btn = button

    def left_click(self, event):
        print(f'LEFT CLICK AT {self.get_cell(event.x, event.y)}')
        if self.is_pressed:

            return  # Don't do anything if the cell is already pressed
        if self.is_mine:
            for cell in Cell.grid:
                # Show all the mines, and disable all buttons
                cell.cell_btn.configure(state="disabled")
                if cell.is_mine:
                    cell.cell_btn.configure(
                        image=self.mine_img, background="red")
        else:
            if self.get_cell_adjacent_mines == 0:
                self.flood_fill()  # Call flood_fill on this cell
            else:
                self.show()  # Show the cell and adjacent mine count
        self.cell_btn.unbind('<Button-1>')
        self.cell_btn.unbind('<Button-3>')

    def get_cell(self, x, y):
        for cell in Cell.grid:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def get_cell_adjacent(self):
        adjacent_cells = [
            # Get the cell itself
            self.get_cell(self.x, self.y),
            # Get the adjacent cells
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x, self.y + 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1)
        ]
        # Remove None values
        return (x for x in adjacent_cells if x is not None)

    @property
    def get_cell_adjacent_mines(self):
        mine_count = 0
        for cell in self.get_cell_adjacent:
            # Ignore cells that are out of bounds
            if cell.is_mine:
                mine_count += 1
        return mine_count

    # If cell is 0, flood fill
    def flood_fill(self):
        queue = [self]
        limit = 30  # set a limit on the number of cells to open
        count = 0    # counter for the number of cells opened
        while queue and count < limit:
            cell = queue.pop(0)
            if not cell.is_pressed:
                cell.show()
                count += 1
                if cell.get_cell_adjacent_mines == 0:
                    for adjacent_cell in cell.get_cell_adjacent:
                        if adjacent_cell is not None and not adjacent_cell.is_pressed:
                            queue.append(adjacent_cell)
    # def show(self):
    #     if not self.is_pressed:
    #         if self.is_mine:
    #             return  # Don't show the cell if it has a mine
    #             # Show the amount of mines around the cell
    #         if self.get_cell_adjacent_mines == 0:
    #             self.cell_btn.configure(
    #                 text="", bg="#e5c29f", state="disabled")
    #             self.cell_btn.configure(
    #                 text=self.get_cell_adjacent_mines, bg="#e5c29f", state="disabled")
    #     self.is_pressed = True

    def show(self):
        if not self.is_pressed:
            if self.is_mine:
                return  # Don't show the cell if it has a mine
            mine_count = self.get_cell_adjacent_mines
            if mine_count == 0:
                self.cell_btn.configure(text=str(
                    " "), anchor="center", font=("Arial", 10, "bold"), compound="center", bd=0, cursor="arrow", bg="#e5c29f", state="disabled")
            else:
                self.cell_btn.configure(text=str(
                    mine_count), anchor="center", font=("Arial", 10, "bold"), compound="center", bd=0, cursor="arrow", bg="#e5c29f", state="disabled")
        self.is_pressed = True

    def flag(self, event):
        print(f'FLAG AT {self.get_cell(event.x, event.y)}')
        if self.is_flagged:
            self.is_flagged = False
            self.cell_btn.configure(
                image="")
        self.is_flagged = True
        self.cell_btn.configure(
            image=self.flag_img, background="red")

    @staticmethod
    def place_mines():
        mines = random.sample(Cell.grid, settings.mine_count)
        for mine in mines:
            mine.is_mine = True

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y})'
