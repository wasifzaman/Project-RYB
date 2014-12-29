'''
'''
from widget_ import Widget_
from tkinter import Frame, Label, Entry, StringVar, LEFT, RIGHT, E, RIDGE, FLAT, DISABLED, NORMAL

class Textbox(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_width = 15
		self.entry_width = 20
		self.stringvar = StringVar()
		self.label = Label(self.widget_frame, width=self.label_width, anchor=E)
		self.entry = Entry(self.widget_frame, width=self.entry_width, textvariable=self.stringvar, relief=FLAT)
		self.label.pack(side=LEFT, padx=3)
		self.entry.pack(side=LEFT)
		self.label_bg, self.label_fg, self.label_hover_bg, self.label_hover_fg = None, None, None, None
		self.entry_bg, self.entry_fg, self.entry_focus_bg, self.entry_focus_fg = '#FFFFFF', None, '#D0F2ED', None
		self.widget_frame.bind('<FocusIn>', lambda event: self.entry.config(bg=self.entry_focus_bg))
		self.widget_frame.bind('<FocusOut>', lambda event: self.entry.config(bg=self.entry_bg))

	#def get_(self):
	#	return self.entry.get()

	def get_info(self):
		return self.label.cget('text'), self.entry.get()

	def settings(self, **kwargs):
		if 'label' in kwargs:
			self.label.config(text=kwargs['label'])
		if 'entry_state' in kwargs:
			self.entry_state = kwargs['entry_state']
			self.entry.config(state=self.entry_state)
		if 'entry' in kwargs:
			if hasattr(self, 'entry_state') and self.entry_state == DISABLED:
				self.entry.config(state=NORMAL)
			self.stringvar.set(kwargs['entry'])
			if hasattr(self, 'entry_state') and self.entry_state == DISABLED:
				self.entry.config(state=DISABLED)
		if 'label_bg' in kwargs:
			self.label_bg = kwargs['label_bg']
			self.label.config(bg=self.label_bg)
		if 'label_fg' in kwargs:
			self.label_fg = kwargs['label_fg']
			self.label.config(fg=self.label_fg)

	def set_input_restriction(self, string):
		def OnValidate(d, i, P, s, S, v, V, W, string):
			if d == 0:
				return True
			accepted_inputs = string.split(',')
			if 'int' in accepted_inputs and S.isdigit():
				return True
			if 'lower' in accepted_inputs:
				S = S.lower()
				return True
			if 'upper' in accepted_inputs:
				S = S.upper()
				return True
			return False

		self.vcmd = self.widget_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', string
		self.entry.config(validate="all", validatecommand=self.vcmd)
		return

	pass