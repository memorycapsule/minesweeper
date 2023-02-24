from tkinter import Button
import random
import settings


class Cell:
    grid = []

    def __init__(self, x, y, is_mine=False, is_flagged=False):
        self.is_mine = is_mine
        self.is_flagged = is_flagged
        self.x = x
        self.y = y
        self.cell_btn = None

        Cell.grid.append(self)

    def create(self, frame):
        button = Button(frame, bg="white",
                        fg="black", width=12, height=4)
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.flag)
        self.cell_btn = button

    def left_click(self, event):
        print(f'LEFT CLICK AT {event.x}, {event.y}')
        if self.is_mine:
            self.cell_btn.configure(bg="red")
        else:
            if self.get_cell_adjacent_mines == 0:
                for cell in self.get_cell_adjacent:
                    if cell is not None:
                        cell.show()
            self.show()

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
        return adjacent_cells

    @property
    def get_cell_adjacent_mines(self):
        mine_count = 0
        for cell in self.get_cell_adjacent:
            # Ignore cells that are out of bounds
            if cell is not None:
                if cell.is_mine:
                    mine_count += 1
        return mine_count

    def show(self):
        adjacent_cells = self.get_cell_adjacent
        for cell in adjacent_cells:
            # Ignore cells that are out of bounds
            if cell is not None:
                if cell.is_mine:
                    return  # Don't show the cell if it has a mine
                else:
                    # Show the amount of mines around the cell
                    cell.cell_btn.configure(
                        text=self.get_cell_adjacent_mines, bg="grey")

    def flag(self, event):
        print(f'FLAG AT {event.x}, {event.y}')
        if self.is_flagged:
            self.is_flagged = False
        self.is_flagged = True

    @staticmethod
    def place_mines():
        mines = random.sample(Cell.grid, settings.mine_count)
        for mine in mines:
            mine.is_mine = True

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y})'
