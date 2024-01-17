from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_lbl_obj = None

    def __init__(self, x, y, is_mine = False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_obj = None

        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            #ext=f"({self.x},{self.y})"
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_obj = btn

    @staticmethod
    def create_cell_count_lable(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            width=12,
            height=4,
            text=f'Cell Count: {Cell.cell_count}',
            font=("", 20)
        )
        Cell.cell_count_lbl_obj = lbl


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            for p in range(settings.CELL_WITHOUT_MINE):
                if self.surrounded_mine_count == 0:
                    for cell_obj in self.surrounded_cell:
                        cell_obj.show_cell()
            #if self.surrounded_mine_count == 0:
            #    for cell_obj in self.surrounded_cell:
            #        cell_obj.show_cell()
            #        if cell_obj.surrounded_mine_count == 0:
            #            for cell_obj2 in cell_obj.surrounded_cell:
            #                cell_obj2.show_cell()
            self.show_cell()
        
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')


    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_obj.configure(text=f'{self.surrounded_mine_count}')
            Cell.cell_count_lbl_obj.configure(text=f"Cell Count: {Cell.cell_count}")
            self.is_opened = True

        self.cell_btn_obj.configure(bg='SystemButtonFace')
        if Cell.cell_count == settings.MINE_COUNT:
            ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You Won.', 'Game Over', 0)
        
    
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cell(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_mine_count(self):
        counter = 0
        for cell in self.surrounded_cell:
            if cell.is_mine:
                counter +=1

        return counter


    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
        #ctypes.windll.user32.MessageBoxW(0, 'You Lose!','Game Over', 0)
        #sys.exit()


    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False

    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINE_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell: ({self.x},{self.y})"