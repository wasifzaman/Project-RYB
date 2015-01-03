import configparser
from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
sys.path.append(os.path.abspath(os.pardir) + '\controllers') #controllers
controllers = os.path.abspath(os.pardir) + '\controllers\\'
images = os.path.abspath(os.pardir) + '\images\\' #image directory

import button
import image
import add_student_
import scan_student_
import student_list_
import toolbox_

''' root window '''
root = Tk()
root.option_add('*Label.Font', 'Helvetica 12')
root.option_add('*TCombobox*Listbox.font', 'Helvetica 11')

''' frame initialization '''
title_frame = Frame(root, bg='#2A2A3D')
button_frame = Frame(root, bg='#2A2A3D')
image_frame = Frame(root, bg='#2A2A3D')

''' frame packing '''
title_frame.pack(fill=BOTH)
button_frame.pack(side=LEFT, fill=BOTH)
image_frame.pack(side=LEFT, fill=BOTH)

''' widgets '''
add_student = button.Button_(button_frame, 0, 0)
scan_student = button.Button_(button_frame, 1, 0)
student_db = button.Button_(button_frame, 2, 0)
export_db = button.Button_(button_frame, 3, 0)
change_lang = button.Button_(button_frame, 4, 0)
print_report = button.Button_(button_frame, 5, 0)
exit = button.Button_(button_frame, 6, 0)
school_image = image.Image_(image_frame, 0, 0)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
add_student.settings(text='Add Student', label_bg=label_bg, hover_bg=hover_bg)
scan_student.settings(text='Scan Student', label_bg=label_bg, hover_bg=hover_bg)
student_db.settings(text='Student Database', label_bg=label_bg, hover_bg=hover_bg)
export_db.settings(text='Export Database', label_bg=label_bg, hover_bg=hover_bg)
change_lang.settings(text='Change Language', label_bg=label_bg, hover_bg=hover_bg)
print_report.settings(text='Print Report', label_bg=label_bg, hover_bg=hover_bg)
exit.settings(text='Exit', label_bg=label_bg, hover_bg=hover_bg)
school_image.settings(image=images + 'background_STU_ELM.jpg')

add_student.label.config(width=30)
scan_student.label.config(width=30)
student_db.label.config(width=30)
export_db.label.config(width=30)
change_lang.label.config(width=30)
print_report.label.config(width=30)
exit.label.config(width=30)

school_image.label.config(bg='#2A2A3D')

add_student.widget_frame.grid(pady=(0, 1))
scan_student.widget_frame.grid(pady=(0, 1))
student_db.widget_frame.grid(pady=(0, 1))
export_db.widget_frame.grid(pady=(0, 1))
change_lang.widget_frame.grid(pady=(0, 1))
print_report.widget_frame.grid(pady=(0, 1))
exit.widget_frame.grid(pady=(0, 1))

add_student.settings(command=add_student_.start_window)
scan_student.settings(command=scan_student_.start_window)
student_db.settings(command=student_list_.start_window)
exit.settings(command=root.destroy)

''' hidden toolbox '''
tool_button = button.Button_(button_frame, 7, 0)
tool_button.settings(text='Toolbox', label_bg=label_bg, hover_bg=hover_bg, command=toolbox_.start_window)
tool_button.label.config(width=30)

root.mainloop()