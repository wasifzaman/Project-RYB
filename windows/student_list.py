from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
images = os.path.abspath(os.pardir) + '\images\\' #image directory
student_images = os.path.abspath(os.pardir) + '\student images\\' #student image directory

import button
import image
import textbox
import date_textbox
import multiline_textbox
import table
import optionmenu
import tkinter.ttk

''' root window '''
student_list = Toplevel()
student_list.option_add('*Label.Font', 'Helvetica 11')
student_list.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
search_frame = Frame(student_list, bg='#2A2A3D')
search_container_frame = Frame(search_frame, bg='#2A2A3D')
notebook_frame = Frame(student_list)
button_frame = Frame(student_list, bg='#2A2A3D')
button_container_frame = Frame(button_frame, bg='#2A2A3D')

''' frame packing '''
search_frame.pack(fill=X)
search_container_frame.pack()
Frame(student_list, bg='#C66100', height=5).pack(fill=X)
notebook_frame.pack()
Frame(student_list, bg='#C66100', height=5).pack(fill=X)
button_frame.pack(fill=X)
button_container_frame.pack()

''' notebook '''
student_info_notebook_1 = tkinter.ttk.Notebook(notebook_frame)

''' style '''
tab_style = tkinter.ttk.Style()
tab_style.configure('TNotebook.Tab', font=('Helvetica', 11))

''' widgets '''
search_value = textbox.Textbox(search_container_frame, 0, 0)
search_type = optionmenu.Optionmenu(search_container_frame, 0, 1)
search_button = button.Button_(search_container_frame, 0, 2)
student_table = table.Table(notebook_frame, 5, 5)
return_button = button.Button_(button_container_frame, 1, 0)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
search_value.settings(label='Search', label_bg='#2A2A3D', label_fg='white')
search_type.settings(label='By', add_option=['Barcode', 'First Name', 'Last Name'], set_option='Barcode', font='Helvetica 11', label_bg='#2A2A3D', label_fg='white')
search_button.settings(text='Search', label_bg=label_bg, hover_bg=hover_bg)
search_value.label.pack(padx=0)
search_type.label.pack(padx=0)
search_button.widget_frame.grid(padx=(5, 0))
return_button.settings(text='Return to Main Menu', label_bg=label_bg, hover_bg=hover_bg)
student_table.settings(sheet_limit=15)

search_value.label.config(width=5)
search_type.label.config(width=2)

return_button.label.config(width=62)

#return_button.widget_frame.grid(pady=(0, 2), columnspan=2)

''' set fill tags '''