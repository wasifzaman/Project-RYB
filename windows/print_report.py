from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory

import button
import textbox
import date_textbox

''' root '''
print_report = Toplevel()
print_report.option_add('*Label.Font', 'Helvetica 11')
print_report.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
print_frame = Frame(print_report)#, bg='#2A2A3D')
button_frame = Frame(print_report, bg='#2A2A3D')
button_container_frame = Frame(button_frame, bg='#2A2A3D')

''' frame packing '''
print_frame.pack(fill=X)
Frame(print_report, bg='#C66100', height=5).pack(fill=X)
button_frame.pack(fill=X)
button_container_frame.pack()

''' widgets '''
print_date = date_textbox.Date_textbox(print_frame, 0, 0)
output_folder = textbox.Textbox(print_frame, 1, 0)
browse_output_folder = button.Button_(print_frame, 1, 1)
cancel_button = button.Button_(button_container_frame, 2, 0)
confirm_button = button.Button_(button_container_frame, 2, 1)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
print_date.settings(label='Date')
output_folder.settings(label='Folder')
browse_output_folder.settings(text='Browse', label_bg=label_bg, hover_bg=hover_bg)
confirm_button.settings(text='Confirm', label_bg=label_bg, hover_bg=hover_bg)
cancel_button.settings(text='Cancel', label_bg=label_bg, hover_bg=hover_bg)

print_date.label.config(width=5)
output_folder.label.config(width=5)

browse_output_folder.label.pack(ipady=5)