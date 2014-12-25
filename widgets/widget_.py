'''
'''
from tkinter import Frame

class Widget_:

	def __init__(self, parent_frame, row, column, width=50, height=50):
		self.widget_frame = Frame(parent_frame, width=width, height=height)
		self.widget_frame.grid(row=row, column=column)
		self.width, self.height = width, height
		return

	def add_tag(self, tag_library, string):
		tag_library[string] = self

	def delete_widget(self):
		for child in self.widget_frame.winfo_children():
			child.destroy()
		self.widget_frame.destroy()

	def hide_widget(self):
		self.widget_frame.grid_forget()

	def get_info(self):
		return

	def set_field(self):
		return

	pass