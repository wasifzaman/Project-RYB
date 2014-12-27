'''
'''
from widget_ import Widget_
from tkinter import Label

class Button_(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_bg, self.label_fg = 'grey', 'white'
		self.hover_bg, self.hover_fg = None, None
		self.label = Label(self.widget_frame, bg=self.label_bg, fg=self.label_fg)
		self.label.pack(ipadx=5, ipady=10)
		
	def get_info(self):
		return self.label.cget('text')

	def settings(self, **kwargs):
		''' all setting changes '''
		
		if 'label_bg' in kwargs:
			self.label_bg = kwargs['label_bg']
			self.label.config(bg=self.label_bg)
		if 'label_fg' in kwargs:
			self.label_fg = kwargs['label_fg']
			self.label.config(fg=self.label_fg)
		if 'text' in kwargs:
			self.label.config(text=kwargs['text'])
		if 'font' in kwargs:
			self.label.config(font=kwargs['font'])
		if 'hover_bg' in kwargs:
			self.hover_bg = kwargs['hover_bg']
			self.hover_fg = self.label_fg if self.hover_fg == None else self.hover_fg
			self.label.bind('<Enter>', lambda event: self.label.config(bg=self.hover_bg, fg=self.hover_fg))
			self.label.bind('<Leave>', lambda event: self.label.config(bg=self.label_bg, fg=self.label_fg))
		if 'hover_fg' in kwargs:
			self.hover_fg = kwargs['hover_fg']
			self.hover_bg = self.label_bg if self.hover_bg == None else self.hover_bg
			self.label.bind('<Enter>', lambda event: self.label.config(fg=self.hover_fg, bg=self.hover_bg))
			self.label.bind('<Leave>', lambda event: self.label.config(fg=self.label_fg, bg=self.label_bg))
		if 'command' in kwargs:
			self.label.bind('<Button-1>', lambda event: kwargs['command']())
		return