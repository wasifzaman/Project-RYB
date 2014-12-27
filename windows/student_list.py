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
search_frame = Frame(student_list)
notebook_frame = Frame(student_list)

''' frame packing '''
search_frame.pack()
notebook_frame.pack()

''' notebook '''
student_info_notebook_1 = tkinter.ttk.Notebook(notebook_frame)

''' style '''
tab_style = tkinter.ttk.Style()
tab_style.configure('TNotebook.Tab', font=('Helvetica', 11))

''' widgets '''
search_value = textbox.Textbox(search_frame, 0, 0)
search_type = optionmenu.Optionmenu(search_frame, 0, 1)
attendance_table = table.Table(notebook_frame, 5, 5)

''' widget settings '''
search_value.settings(label='Search')
search_type.settings(label='By', add_option=['Barcode', 'First Name', 'Last Name'], set_option='Barcode', font='Helvetica 11')

search_value.label.config(width=5)
search_type.label.config(width=2)

''' set fill tags '''

#student_list.mainloop()