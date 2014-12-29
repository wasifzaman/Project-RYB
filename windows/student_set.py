from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory

import button
import table

def start_window(student_info_set):
	''' root window '''
	student_set = Toplevel()
	student_set.option_add('*Label.Font', 'Helvetica 11')

	''' frame initialization '''
	student_table_frame = Frame(student_set)
	button_frame = Frame(student_set, bg='#2A2A3D')
	button_container_frame = Frame(button_frame, bg='#2A2A3D')

	''' frame packing '''
	student_table_frame.pack()
	Frame(student_set, bg='#C66100', height=5).pack(fill=X)
	button_frame.pack(fill=X)
	button_container_frame.pack()

	''' widgets '''
	student_table = table.Table(student_table_frame, 0, 0)
	add_button = button.Button_(button_container_frame, 0, 0)
	return_button = button.Button_(button_container_frame, 1, 0)

	''' hover button colors '''
	label_bg = '#1C528A'
	hover_bg = '#2C82DB'

	''' widget settings '''
	student_table.settings(sheet_limit=10, add_row=['Barcode', 'First Name', 'Last Name', 'Chinese Name', 'Date of Birth'])
	add_button.settings(text='Select Student', label_bg=label_bg, hover_bg=hover_bg)
	return_button.settings(text='Return to Main Menu', label_bg=label_bg, hover_bg=hover_bg)

	add_button.label.config(width=30)
	return_button.label.config(width=30)

	add_button.widget_frame.grid(pady=1)
	return_button.widget_frame.grid(pady=(0, 1))

	''' add row to table '''
	for student_info in student_info_set:
		student_table.settings(add_row=student_info)

	student_set.mainloop()