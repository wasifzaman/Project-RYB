'''
'''
from tkinter import *
from widget_ import Widget_
from datetime import datetime

class Date_textbox(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_width = 15
		self.mdy_frame = 20
		self.entry_width = 5
		self.dash_width = 1
		self.month_stringvar = StringVar()
		self.date_stringvar = StringVar()
		self.year_stringvar = StringVar()
		self.label = Label(self.widget_frame, width=self.label_width, anchor=E)
		self.mdy_frame = Frame(self.widget_frame, width=self.mdy_frame, bg='white', relief=FLAT, bd=1)
		self.month_entry = Entry(self.mdy_frame, width=self.entry_width, textvariable=self.month_stringvar, bd=0, justify=CENTER)
		self.day_entry = Entry(self.mdy_frame, width=self.entry_width, textvariable=self.date_stringvar, bd=0, justify=CENTER)
		self.year_entry = Entry(self.mdy_frame, width=self.entry_width + 1, textvariable=self.year_stringvar, bd=0, justify=CENTER)
		self.dash_one = Label(self.mdy_frame, text='/', bg='white', width=self.dash_width)
		self.dash_two = Label(self.mdy_frame, text='/', bg='white', width=self.dash_width)
		self.label.pack(side=LEFT, padx=3)
		self.mdy_frame.pack(side=LEFT)
		self.month_entry.pack(side=LEFT)
		self.dash_one.pack(side=LEFT)
		self.day_entry.pack(side=LEFT)
		self.dash_two.pack(side=LEFT)
		self.year_entry.pack(side=LEFT)
		self.label_bg, self.label_fg, self.label_hover_bg, self.label_hover_fg = None, None, None, None
		self.entry_bg, self.entry_fg, self.entry_hover_bg, self.entry_hover_fg = None, None, None, None

		def OnValidate(d, i, P, s, S, v, V, W, digit_type):
			if d == '0':
				if len(P) == 0:
					if digit_type == 'year':
						self.day_entry.focus_set()
					elif digit_type == 'day':
						self.month_entry.focus_set()
				return True

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

	#def get_(self):
	#	date = self.month_entry.get() + '/' + self.day_entry.get() + '/' + self.year_entry.get()
	#	return datetime.strptime(date, '%m/%d/%Y')

	def get_info(self):
		date = self.month_entry.get() + '/' + self.day_entry.get() + '/' + self.year_entry.get()
		return date, datetime.strptime(date, '%m/%d/%Y')

	def settings(self, **kwargs):
		if 'label' in kwargs:
			self.label.config(text=kwargs['label'])
		if 'entry_state' in kwargs:
			self.entry_state = kwargs['entry_state']
			self.month_entry.config(state=self.entry_state)
			self.day_entry.config(state=self.entry_state)
			self.year_entry.config(state=self.entry_state)
		if 'date' in kwargs:
			#expects a full datetime string entry ex: 2014-12-31 00:00:00
			if hasattr(self, 'entry_state') and self.entry_state == DISABLED:
				self.month_entry.config(state=NORMAL)
				self.day_entry.config(state=NORMAL)
				self.year_entry.config(state=NORMAL)
			date = kwargs['date'][:10].split('-')
			y, m, d = date[0], date[1], date[2]
			self.month_entry.delete(0, END)
			self.day_entry.delete(0, END)
			self.year_entry.delete(0, END)
			self.month_entry.insert(0, m)
			self.day_entry.insert(0, d)
			self.year_entry.insert(0, y)
			if hasattr(self, 'entry_state') and self.entry_state == DISABLED:
				self.month_entry.config(state=DISABLED)
				self.day_entry.config(state=DISABLED)
				self.year_entry.config(state=DISABLED)

	pass



'''
t = Tk()
f = Frame(width=500, height=500)
f.pack()

d = Date_entry(f, 0, 0)
d.set_text_field(date='10/07/1988')

b = Button(f, text='abcd')
b.place(x=50, y=50)
b.config(command=lambda: print(d.get_info()))

d.month_entry.config(font='11')
d.day_entry.config(font='11')
d.year_entry.config(font='11')
d.dash_one.config(font='11')
d.dash_two.config(font='11')

t.mainloop()
'''

'''
date_entry example

test_var = StringVar()
test_entry = Entry(content, textvariable=test_var)
test_entry.pack()

def var_change(*args):
	def OnValidate(d, i, P, s, S, v, V, W):
		if len(s) == 10: return False
		if S == '/': return True
		elif not S.isdigit():
			return False
		return True

	test_entry.config(validate="key", validatecommand=(content.register(OnValidate),
		'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

	if len(test_var.get()) == 1 and (not test_var.get().isdigit()):
		test_var.set('')
	elif len(test_var.get()) == 2:
		test_entry.insert(2, '/')
	elif len(test_var.get()) == 5:
		test_entry.insert(5, '/')
	return

test_var.trace('w', var_change)

'''