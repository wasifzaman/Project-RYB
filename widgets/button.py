'''
'''
from widget_ import Widget_
from tkinter import Label, W
from PIL import Image, ImageTk

class Button_(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_bg, self.label_fg = 'grey', 'white'
		self.hover_bg, self.hover_fg = None, None
		self.label = Label(self.widget_frame, bg=self.label_bg, fg=self.label_fg)
		self.label.grid(row=0, column=1, ipadx=5, ipady=10)
		
	def get_info(self):
		return self.label.cget('text')

	def set_hover(self):
		def set_hover_bg(event):
			self.label.config(bg=self.hover_bg, fg=self.hover_fg)
			self.img.config(bg=self.hover_bg, fg=self.hover_fg)

		def remove_hover_bg(event):
			self.label.config(bg=self.label_bg, fg=self.label_fg)
			self.img.config(bg=self.label_bg, fg=self.label_fg)

		if hasattr(self, 'img'):
			self.widget_frame.bind('<Enter>', set_hover_bg)
			self.widget_frame.bind('<Leave>', remove_hover_bg)
		else:
			self.widget_frame.bind('<Enter>', lambda event: self.label.config(bg=self.hover_bg, fg=self.hover_fg))
			self.widget_frame.bind('<Leave>', lambda event: self.label.config(bg=self.label_bg, fg=self.label_fg))

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
			self.set_hover()
		if 'hover_fg' in kwargs:
			self.hover_fg = kwargs['hover_fg']
			self.hover_bg = self.label_bg if self.hover_bg == None else self.hover_bg
			self.set_hover()
		if 'command' in kwargs:
			self.command = kwargs['command']
			self.label.bind('<Button-1>', lambda event: self.command())
			if hasattr(self, 'img'):
				self.img.bind('<Button-1>', lambda event: self.command())
		if 'image' in kwargs:
			self.img_path = kwargs['image']
			self.picture = Image.open(self.img_path)
			self.image = ImageTk.PhotoImage(self.picture)
			self.img = Label(self.widget_frame, bg=self.label_bg, fg=self.label_fg)
			self.img.grid(row=0, column=0, ipadx=5, ipady=5, columnspan=2, sticky=W)
			self.img.config(image=self.image)
			self.set_hover()
			if hasattr(self, 'command'):
				self.img.bind('<Button-1>', lambda event: self.command())
		if 'image_resize' in kwargs:
			self.picture = self.picture.resize(kwargs['image_resize'], Image.ANTIALIAS)
			self.image = ImageTk.PhotoImage(self.picture)
			self.img.config(image=self.image)
		return