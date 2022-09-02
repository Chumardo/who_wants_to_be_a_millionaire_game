from curses import window
from tkinter import *

window = Tk()
window.title("Who wants to be a millionaire?")
window.configure(bg="black")
window.iconphoto(False, PhotoImage(file='Images/icon.png'))
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))


window.mainloop()