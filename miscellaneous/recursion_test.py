from tkinter import *


r = Tk()


f1 = Frame(r)
f2 = Frame(r)

ff1 = Frame(f1)
ff2 = Frame(f2)

ff3 = Label(ff1)

_list = []

def find_all(root):
	if len(root.winfo_children()) == 0:
		return
	else:
		for child in root.winfo_children():
			_list.append(root)
			find_all(child)

find_all(r)

print(_list)