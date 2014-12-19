'''
'''
from widget_ import Widget_
from tkinter import *

class Table(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.canvas = Canvas(self.widget_frame)
		self.table_frame = Frame(self.canvas, bg='black')
		self.y_scrollbar = Scrollbar(self.widget_frame)
		self.x_scrollbar = Scrollbar(self.widget_frame, orient=HORIZONTAL)
		self.navigate_frame = Frame(self.widget_frame)
		self.left = Button(self.navigate_frame, text='<', relief=GROOVE)
		self.right = Button(self.navigate_frame, text='>', relief=GROOVE)
		self.y_scrollbar.config(command=self.canvas.yview)
		self.x_scrollbar.config(command=self.canvas.xview)
		self.canvas.grid()
		self.table_frame.pack()
		self.y_scrollbar.grid(row=0, column=1)
		self.x_scrollbar.grid(row=1, column=0)
		self.navigate_frame.grid(row=2, columnspan=2)
		self.right.pack(side=RIGHT)
		self.left.pack(side=RIGHT)
		self.current_row = 0
		self.rows = []

	def settings(self, **kwargs):
		''' all setting changes '''

		if 'add_row' in kwargs:
			row = []
			for cell_text in kwargs['add_row']:
				row.append(Label(self.table_frame, bg='white', text=cell_text))

			current_col = 0
			for cell in row:
				if self.current_row == 0 and current_col == 0:
					cell.grid(row=self.current_row, column=current_col, padx=1, pady=1, sticky=EW)
				elif current_col == 0:
					cell.grid(row=self.current_row, column=current_col, padx=1, pady=(0, 1), sticky=EW)
				else:
					cell.grid(row=self.current_row, column=current_col, padx=(0, 1), sticky=EW)
				current_col += 1

			self.rows.append(row)
			self.current_row += 1
		return