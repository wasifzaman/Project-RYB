'''
'''
from textbox import Textbox
from tkinter.scrolledtext import ScrolledText
from tkinter import END, LEFT, RIDGE

class Multiline_textbox(Textbox):

	def __init__(self, parent_frame, x, y):
		Textbox.__init__(self, parent_frame, x, y)
		self.entry.pack_forget()
		self.entry = ScrolledText(self.widget_frame, width=self.entry_width, relief=RIDGE)
		self.entry.pack(side=LEFT)

	def get_info(self):
		return self.label.cget('text'), self.entry.get('1.0', END+'-1c')

	def settings(self, **kwargs):
		if 'label' in kwargs:
			self.label.config(text=kwargs['label'])
		if 'entry' in kwargs:
			self.entry.delete('1.0', END)
			self.entry.insert('1.0', kwargs['entry'])
		if 'height' in kwargs:
			self.entry.config(height=kwargs['height'])
		if 'entry_width' in kwargs:
			self.entry.config(width=kwargs['entry_width'])