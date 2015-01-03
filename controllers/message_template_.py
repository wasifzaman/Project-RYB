import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
images = os.path.abspath(os.pardir) + '\images\\' #image directory
#controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
from imp import reload
import add_widget_get_
import add_widget_set
#import db_test

def start_window(text, buttons, wraplength=False, message_img=False, title_=''):
	import message_template
	import button
	import image

	if not hasattr(message_template, 'load_state'):
		setattr(message_template, 'load_state', True)
	else:
		reload(message_template)

	message_template.message_.config(text=text)

	buttons_ = {}

	def return_():
		message_template.message.destroy()

	column_num = 0
	for button_text in buttons:
		buttons_[button_text] = button.Button_(message_template.button_container_frame, 0, column_num)
		buttons_[button_text].settings(text=button_text, label_bg=message_template.label_bg, hover_bg=message_template.hover_bg)
		buttons_[button_text].settings(command=return_)
		column_num += 1

	if wraplength: message_template.message_.config(wraplength=wraplength)
	if message_img:
		message_template.image_.settings(image=message_img, resize=(50, 50))
		message_template.image_frame.grid(row=1, column=0, sticky=E+W+N+S)
	
	message_template.title.config(text=title_)

	def start_move(event):
		setattr(message_template.title, 'drag_x', event.x)
		setattr(message_template.title, 'drag_y', event.y)

	def in_motion(event):
		delta_x = event.x - message_template.title.drag_x
		delta_y = event.y - message_template.title.drag_y
		x = message_template.message.winfo_x() + delta_x
		y = message_template.message.winfo_y() + delta_y
		message_template.message.geometry("+%s+%s" % (x, y))

	message_template.title.bind('<ButtonPress-1>', start_move)
	message_template.title.bind('<B1-Motion>', in_motion)



	message_template.message.mainloop()

start_window('Would you like to continue?',
	['Yes', 'No', 'Cancel'],
	message_img=images + 'Warning-Shield-128.png',
	wraplength=1000,
	title_='Test')