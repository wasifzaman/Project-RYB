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

import ttkNotebook_style

''' root window '''
scan_student = Toplevel()
scan_student.option_add('*Label.Font', 'Helvetica 11')
scan_student.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
search_frame = Frame(scan_student, bg='#2A2A3D')
search_container_frame = Frame(search_frame, bg='#2A2A3D')
notebook_frame = Frame(scan_student, bg='#2A2A3D')
button_frame = Frame(scan_student, bg='#2A2A3D')
button_container_frame = Frame(button_frame, bg='#2A2A3D')

''' frame packing '''
search_frame.pack(fill=X)
search_container_frame.pack()
Frame(scan_student, bg='#C66100', height=5).pack(fill=X)
notebook_frame.pack()
Frame(scan_student, bg='#C66100', height=5).pack(fill=X)
button_frame.pack(fill=X)
button_container_frame.pack()

''' notebook '''
student_info_notebook_1 = tkinter.ttk.Notebook(notebook_frame)
student_info_notebook_2 = tkinter.ttk.Notebook(notebook_frame)
notes_notebook = tkinter.ttk.Notebook(notebook_frame)
attendance_notebook = tkinter.ttk.Notebook(notebook_frame)
message_notebook = tkinter.ttk.Notebook(notebook_frame)
#portrait_notebook = tkinter.ttk.Notebook(notebook_frame)
general = Frame(student_info_notebook_1)
address = Frame(student_info_notebook_1)
contact = Frame(student_info_notebook_1)
payment = Frame(student_info_notebook_2)
notes = Frame(notes_notebook)
message = Frame(message_notebook, bg='yellow')
attendance = Frame(attendance_notebook)
#portrait = Frame(portrait_notebook)
student_info_notebook_1.grid(row=0, column=0)
student_info_notebook_2.grid(row=1, column=0, sticky=N)
notes_notebook.grid(row=1, column=1, sticky=N+W)
attendance_notebook.grid(row=0, column=2, rowspan=2, sticky=NW)
message_notebook.grid(row=0, column=1, sticky=NW+E+S)
#portrait_notebook.grid(row=0, column=1, sticky=W)
student_info_notebook_1.add(general, text='General')
student_info_notebook_1.add(address, text='Address')
student_info_notebook_1.add(contact, text='Contact')
student_info_notebook_2.add(payment, text='Payment')
notes_notebook.add(notes, text='Notes')
message_notebook.add(message, text='Message Center')
attendance_notebook.add(attendance, text='Attendance Table')
#portrait_notebook.add(portrait, text='Photo')

''' widgets '''
search_value = textbox.Textbox(search_container_frame, 0, 0)
search_type = optionmenu.Optionmenu(search_container_frame, 0, 1)
search_button = button.Button_(search_container_frame, 0, 2)
first_name = textbox.Textbox(general, 0, 0)
last_name = textbox.Textbox(general, 1, 0)
chinese_name = textbox.Textbox(general, 2, 0)
date_of_birth = date_textbox.Date_textbox(general, 3, 0)
age = textbox.Textbox(general, 4, 0)
gender = textbox.Textbox(general, 5, 0)
card_printed = textbox.Textbox(general, 6, 0)
barcode = textbox.Textbox(payment, 6, 0)
tuition_paid_day = date_textbox.Date_textbox(payment, 7, 0)
total = textbox.Textbox(payment, 8, 0)
amount_owed = textbox.Textbox(payment, 9, 0)
service_type = textbox.Textbox(payment, 10, 0)
classes_awarded = textbox.Textbox(payment, 11, 0)
classes_remaining = textbox.Textbox(payment, 12, 0)
regular_class_time = textbox.Textbox(payment, 13, 0)
address_ = textbox.Textbox(address, 0, 0)
city = textbox.Textbox(address, 1, 0)
state = textbox.Textbox(address, 2, 0)
zipcode = textbox.Textbox(address, 3, 0)
email = textbox.Textbox(address, 4, 0)
parent_full_name = textbox.Textbox(contact, 5, 0)
pick_up_person = textbox.Textbox(contact, 6, 0)
home_phone = textbox.Textbox(contact, 7, 0)
cell_phone_1 = textbox.Textbox(contact, 8, 0)
cell_phone_2 = textbox.Textbox(contact, 9, 0)
notes_ = multiline_textbox.Multiline_textbox(notes, 10, 0)
attendance_table = table.Table(attendance, 5, 5)
create_payment = button.Button_(button_container_frame, 0, 0)
check_in_button = button.Button_(button_container_frame, 0, 1)
return_button = button.Button_(button_container_frame, 1, 0)
#portrait_ = image.Image_(portrait, 0, 0)

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
first_name.settings(label='First Name')
last_name.settings(label='Last Name')
chinese_name.settings(label='Chinese Name')
date_of_birth.settings(label='Date of Birth')
age.settings(label='Age')
gender.settings(label='Gender')
card_printed.settings(label='Card Printed?')
barcode.settings(label='Barcode')
tuition_paid_day.settings(label='Tuition Paid Day')
total.settings(label='Total Amount')
amount_owed.settings(label='Amount Owed')
service_type.settings(label='Service Type')
classes_awarded.settings(label='Classes Awarded')
classes_remaining.settings(label='Classes Remaining')
regular_class_time.settings(label='Class Time')
address_.settings(label='Address')
city.settings(label='City')
state.settings(label='State')
zipcode.settings(label='Zip Code')
email.settings(label='E-mail')
parent_full_name.settings(label='Parent Name')
pick_up_person.settings(label='Pick Up Person')
home_phone.settings(label='Home Phone')
cell_phone_1.settings(label='Cell Phone 1')
cell_phone_2.settings(label='Cell Phone 2')
notes_.settings(height=11, entry_width=36)
notes_.entry.config(font='Helvetica 11')
notes_.label.pack_forget()
create_payment.settings(text='Add Payment', label_bg=label_bg, hover_bg=hover_bg)
check_in_button.settings(text='Check In Student', label_bg=label_bg, hover_bg=hover_bg)
return_button.settings(text='Return to Main Menu', label_bg=label_bg, hover_bg=hover_bg)
attendance_table.settings(sheet_limit=10)
attendance_table.widget_frame.config(bg='#2A2A3D')
attendance_table.navigate_frame.config(bg='#2A2A3D')
attendance_table.first.config(bg='#2A2A3D', fg='white')
attendance_table.last.config(bg='#2A2A3D', fg='white')
attendance_table.left.config(bg='#2A2A3D', fg='white')
attendance_table.right.config(bg='#2A2A3D', fg='white')
attendance_table.go_to_button.config(bg='#2A2A3D', fg='white')
attendance_table.go_to.config(font='Helvetica 11')
#portrait_.settings(image=student_images + 'null_portrait.jpg', resize=(135, 135))

zipcode.set_input_restriction('int')
home_phone.set_input_restriction('int')
cell_phone_1.set_input_restriction('int')
cell_phone_2.set_input_restriction('int')

search_value.label.config(width=5)
search_type.label.config(width=2)
create_payment.label.config(width=30)
check_in_button.label.config(width=30)
return_button.label.config(width=62)

create_payment.widget_frame.grid(pady=2, padx=1)
check_in_button.widget_frame.grid(padx=1)
return_button.widget_frame.grid(pady=(0, 2), columnspan=2)

attendance_table.widget_frame.grid(rowspan=2, sticky=N+S)

search_value.set('BRK-005')
''' set fill tags '''