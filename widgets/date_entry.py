'''
'''
from widget_ import Widget_
from datetime import datetime

class Date_entry(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_width = 20
		self.mdy_frame = 30
		self.entry_width = 10
		self.month_stringvar = StringVar()
		self.date_stringvar = StringVar()
		self.year_stringvar = StringVar()
		self.label = Label(self.widget_frame, width=self.label_width)
		self.mdy_frame = Frame(self.widget_frame, width=self.mdy_frame, bg='white', relief=RIDGE, bd=1)
		self.month_entry = Entry(self.mdy_frame, width=self.entry_width, textvariable=self.month_stringvar, bd=0, justify=CENTER)
		self.day_entry = Entry(self.mdy_frame, width=self.entry_width, textvariable=self.date_stringvar, bd=0, justify=CENTER)
		self.year_entry = Entry(self.mdy_frame, width=self.entry_width, textvariable=self.year_stringvar, bd=0, justify=CENTER)
		self.dash_one = Label(self.mdy_frame, text='/', bg='white')
		self.dash_two = Label(self.mdy_frame, text='/', bg='white')
		self.label.pack(side=LEFT)
		self.mdy_frame.pack(side=LEFT)
		self.month_entry.pack(side=LEFT)
		self.dash_one.pack(side=LEFT)
		self.day_entry.pack(side=LEFT)
		self.dash_two.pack(side=LEFT)
		self.year_entry.pack(side=LEFT)
		self.label_bg, self.label_fg, self.label_hover_bg, self.label_hover_fg = None, None, None, None
		self.entry_bg, self.entry_fg, self.entry_hover_bg, self.entry_hover_fg = None, None, None, None

		def OnValidate(d, i, P, s, S, v, V, W, digit_type):
			if d == 0: return True
			if S.isdigit() and ( \
					(digit_type == 'month' and len(P) > 2) or \
					(digit_type == 'day' and len(P) > 2) or \
					(digit_type == 'year' and len(P) > 4)):
					return False

			elif S.isdigit():
				if len(P) == 2 and digit_type == 'month':
					self.day_entry.focus_set()
				elif len(P) == 2 and digit_type == 'day':
					self.year_entry.focus_set()
				return True
			return False


		self.month_entry.config(validate="all", validatecommand=(self.mdy_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'month'))
		self.day_entry.config(validate="all", validatecommand=(self.mdy_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'day'))
		self.year_entry.config(validate="all", validatecommand=(self.mdy_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'year'))

	def get_info(self):
		date = self.month_entry.get() + '/' + self.day_entry.get() + '/' + self.year_entry.get()
		return date, datetime.strptime(date, '%m/%d/%Y')

	def set_text_field(self, label=False, date=False):
		if label:
			self.label.config(text=label)
		elif date:
			date = date.split('/')
			m, d, y = date[0], date[1], date[2]
			self.month_entry.delete(0, END)
			self.day_entry.delete(0, END)
			self.year_entry.delete(0, END)
			self.month_entry.insert(0, m)
			self.day_entry.insert(0, d)
			self.year_entry.insert(0, y)

	pass

from tkinter import *


t = Tk()
f = Frame(width=500, height=500)
f.pack()

d = Date_entry(f, 0, 0)
d.set_text_field(date='10/07/1988')

b = Button(f, text='abcd')
b.place(x=50, y=50)
b.config(command=lambda: print(d.get_info()))

t.mainloop()

"1ZX799450325526838"