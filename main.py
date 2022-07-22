from tkinter import *
import settings
import utils
root = Tk()
# Override the settings of the root window

root.configure(background='#000')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('MineSweeper Game')  # Title of the game 
root.resizable(False, False)  

top_frame = Frame(
    root,
    bg='black',
    width=1080,
    height=180,
)

top_frame.place(x=0, y=0)

left_frame = Frame(

    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)

left_frame.place(x=0, y=180)
# Run the window


center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)

center_frame.place(x=utils.width_prct(25),
                   y=utils.height_prct(25)
                   )
root.mainloop() 
