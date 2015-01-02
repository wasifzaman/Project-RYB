'''
'''
from widget_ import Widget_
from tkinter import Frame, Label, Entry, StringVar, LEFT, RIGHT, E, RIDGE
import tkinter.ttk as ttk

class Optionmenu(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_width = 15
		self.entry_width = 20
		self.options = []
		self.stringvar = StringVar()
		self.label = Label(self.widget_frame, width=self.label_width, anchor=E)
		self.combobox = ttk.Combobox(self.widget_frame,
			textvariable=self.stringvar,
			state='readonly'
			)
		self.label.pack(side=LEFT, padx=3)
		self.combobox.pack(side=LEFT)
		self.label_bg, self.label_fg, self.label_hover_bg, self.label_hover_fg = None, None, None, None
		self.entry_bg, self.entry_fg, self.entry_hover_bg, self.entry_hover_fg = None, None, None, None
		self.combobox_style = ttk.Style()
		self.combobox_style.configure(
			'TCombobox',
			background='white',
			selectbackground='white',
			selectforeground='black',
			borderwidth=0
			)
		self.combobox_style.map('TCombobox', fieldbackground=[])

	def settings(self, **kwargs):
		if 'label' in kwargs:
			self.label.config(text=kwargs['label'])
		if 'set_option' in kwargs:
			self.stringvar.set(kwargs['set_option'])
		if 'add_option' in kwargs:
			if type(kwargs['add_option']) == list:
				self.options.extend(kwargs['add_option'])
			elif type(kwargs['add_option']) == str:
				self.options.append(kwargs['add_option'])
			self.combobox['values'] = tuple(self.options)
		if 'font' in kwargs:
			self.combobox.config(font=kwargs['font'])
		if 'label_bg' in kwargs:
			self.label_bg = kwargs['label_bg']
			self.label.config(bg=self.label_bg)
		if 'label_fg' in kwargs:
			self.label_fg = kwargs['label_fg']
			self.label.config(fg=self.label_fg)


	pass