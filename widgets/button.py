'''
'''
from widget_ import Widget_
from tkinter import Label

class Button_(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label = Label(self.widget_frame)
		self.label.pack()
		self.label_bg, self.label_fg = None, None

	def get_info(self):
		return self.label.cget('text')

	def settings(self, **kwargs):
		''' all setting changes '''
		
		if 'label_bg' in kwargs:
			self.label.config(bg=kwargs['label_bg'])
		if 'label_fg' in kwargs:
			self.label.config(fg=kwargs['label_fg'])
		if 'text' in kwargs:
			self.label.config(text=kwargs['text'])
		if 'font' in kwargs:
			self.label.config(font=kwargs['font'])
		return