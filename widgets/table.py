'''
'''
from widget_ import Widget_
from tkinter import *

class Table(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.canvas = Canvas(self.widget_frame)
		self.header_frame = Frame(self.canvas, bg='black')
		self.table_frame = Frame(self.canvas)
		self.y_scrollbar = Scrollbar(self.widget_frame)
		self.x_scrollbar = Scrollbar(self.widget_frame, orient=HORIZONTAL)
		self.navigate_frame = Frame(self.widget_frame)
		self.first = Button(self.navigate_frame, text='<<', relief=GROOVE)
		self.left = Button(self.navigate_frame, text='<', relief=GROOVE)
		self.right = Button(self.navigate_frame, text='>', relief=GROOVE)
		self.last = Button(self.navigate_frame, text='>>', relief=GROOVE)
		self.go_to = Entry(self.navigate_frame, relief=GROOVE, width=2)
		self.go_to_button = Button(self.navigate_frame, text='Go', relief=GROOVE)
		self.y_scrollbar.config(command=self.canvas.yview)
		self.x_scrollbar.config(command=self.canvas.xview)
		self.canvas.grid()
		self.header_frame.pack(anchor=W)
		self.table_frame.pack()
		self.y_scrollbar.grid(row=0, column=1)
		self.x_scrollbar.grid(row=1, column=0)
		self.navigate_frame.grid(row=2, columnspan=2)
		self.go_to.pack(side=LEFT)
		self.go_to_button.pack(side=LEFT)
		self.last.pack(side=RIGHT)
		self.right.pack(side=RIGHT)
		self.left.pack(side=RIGHT)
		self.first.pack(side=RIGHT)
		self.current_row = 0
		self.rows = []
		self.sheets = [Frame(self.table_frame, bg='black')]
		self.sheet_limit = False
		self.font = False
		self.current_sheet = 0
		self.sheets[0].pack()
		self.column_widths = {}

		def go_to_sheet(button):
			def delete_cur_sheet():
				#for child in self.sheets[self.current_sheet].winfo_children():
				#	child.destroy()
				self.sheets[self.current_sheet].pack_forget()

			if button == '+1':
				if self.current_sheet + 1 >= len(self.sheets): return
				delete_cur_sheet()
				self.current_sheet += 1
				self.sheets[self.current_sheet].pack()

			elif button == '-1':
				if self.current_sheet - 1 < 0: return
				delete_cur_sheet()
				self.current_sheet -= 1
				self.sheets[self.current_sheet].pack()

			elif button == 'last':
				if self.current_sheet + 1 == len(self.sheets): return
				delete_cur_sheet()
				self.current_sheet = len(self.sheets) - 1
				self.sheets[self.current_sheet].pack()

			elif button == 'first':
				if self.current_sheet == 0: return
				delete_cur_sheet()
				self.current_sheet = 0
				self.sheets[self.current_sheet].pack()

			elif button.isdigit():
				page_num = int(button)
				if page_num >= 0 and page_num < len(self.sheets) and self.current_sheet != page_num:
					delete_cur_sheet()
					self.current_sheet = page_num
					self.sheets[self.current_sheet].pack()

		def goto_entry_validation(d, i, P, s, S, v, V, W):
			if d == 0: return True
			elif S.isdigit():
				return True
			return False

		self.first.config(command=lambda: go_to_sheet('first'))
		self.right.config(command=lambda: go_to_sheet('+1'))
		self.left.config(command=lambda: go_to_sheet('-1'))
		self.last.config(command=lambda: go_to_sheet('last'))
		self.go_to_button.config(command=lambda: go_to_sheet(self.go_to.get()))

		self.go_to.config(validate="all", validatecommand=(self.widget_frame.register(goto_entry_validation),
				'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

	def settings(self, **kwargs):
		''' all setting changes '''

		if 'add_row' in kwargs:
			if len(self.column_widths) == 0:
				self.column_widths = {kwargs['add_row'].index(item_): 0 for item_ in kwargs['add_row']}

			if self.sheet_limit and self.current_row == self.sheet_limit:
				self.sheets.append(Frame(self.table_frame, bg='black'))
				self.current_row = 0
			
			row = []
			for cell_text in kwargs['add_row']:
				row.append(Label(self.sheets[-1], bg='white', text=cell_text))

			current_col = 0

			for cell in row:
				if self.current_row == 0 and current_col == 0:
					cell.grid(row=self.current_row, column=current_col, padx=1, pady=1, sticky=EW)
				elif current_col == 0:
					cell.grid(row=self.current_row, column=current_col, padx=1, pady=(0, 1), sticky=EW)
				else:
					cell.grid(row=self.current_row, column=current_col, padx=(0, 1), sticky=EW)

				#adjust width
				if len(cell.cget('text')) > self.column_widths[current_col]:
					self.column_widths[current_col] = len(cell.cget('text'))
					cell.config(width=self.column_widths[current_col])
					if hasattr(self, 'headers'):
						self.headers[current_col].config(width=self.column_widths[current_col])
				elif len(cell.cget('text')) <= self.column_widths[current_col]:
					cell.config(width=self.column_widths[current_col])
				current_col += 1

			self.rows.append(row)
			self.current_row += 1
		if 'remove_row' in kwargs:
			return
		if 'sheet_limit' in kwargs:
			self.sheet_limit = kwargs['sheet_limit']
		if 'font' in kwargs:
			for row in self.rows:
				for label in row:
					label.config(font=kwargs['font'])
		if 'add_header' in kwargs:
			if len(self.column_widths) == 0:
				self.column_widths = {kwargs['add_header'].index(item_): len(item_) for item_ in kwargs['add_header']}

			self.headers = []
			for cell_text in kwargs['add_header']:
				self.headers.append(Label(self.header_frame, bg='#0198E1', text=cell_text))

			current_col = 0

			for cell in self.headers:
				if current_col == 0:
					cell.grid(row=0, column=current_col, padx=1, pady=(1, 0), sticky=E+W)
				else:
					cell.grid(row=0, column=current_col, padx=(0, 1), pady=(1, 0), sticky=E+W)
				cell.config(width=self.column_widths[current_col])
				current_col += 1

		return