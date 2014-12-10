'''
'''
from textbox_widget import Textbox

class Date_entry(Textbox):

	pass

from tkinter import *


t = Tk()
f = Frame(width=500, height=500)
f.pack()

d = Date_entry(f, 0, 0)
d.set_input_restriction(None)


t.mainloop()

"1ZX799450325526838"