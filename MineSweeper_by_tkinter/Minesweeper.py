from tkinter import *
import settings
import Utils
from Cell_settings import Cell

root = Tk()

root.configure(bg='black')
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=Utils.height_prct(25),
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=Utils.width_prct(25),
    height=Utils.height_prct(75)
)
left_frame.place(
    x=0,
    y=Utils.height_prct(25)
)

center_frame = Frame(
    root,
    bg='black',
    width=Utils.width_prct(75),
    height=Utils.height_prct(75)
)
center_frame.place(
    x=Utils.width_prct(25),
    y=Utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(row=x, column=y)

Cell.randomize_mines()

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text="Minesweeper",
    font=("", 40)
)
game_title.place(
    x=Utils.width_prct(35),
    y=0
)

Cell.create_cell_count_lable(left_frame)
Cell.cell_count_lbl_obj.place(x=0, y=0)

root.mainloop()