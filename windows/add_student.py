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
import optionmenu
import add_widget_get_
import tkinter.ttk

''' root window '''
add_student = Tk()
add_student.option_add('*Label.Font', 'Helvetica 11')
add_student.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
notebook_frame = Frame(add_student)

''' frame packing '''
notebook_frame.pack()

''' notebook '''
student_info_notebook_1 = tkinter.ttk.Notebook(notebook_frame)
student_info_notebook_2 = tkinter.ttk.Notebook(notebook_frame)
notes_notebook = tkinter.ttk.Notebook(notebook_frame)
portrait_notebook = tkinter.ttk.Notebook(notebook_frame)
general = Frame(student_info_notebook_1)
address = Frame(student_info_notebook_1)
contact = Frame(student_info_notebook_1)
payment = Frame(student_info_notebook_2)
notes = Frame(notes_notebook)
portrait = Frame(portrait_notebook)
student_info_notebook_1.grid(row=0, column=0)
student_info_notebook_2.grid(row=1, column=0)
notes_notebook.grid(row=2, column=0, sticky=W)
portrait_notebook.grid(row=0, column=1, sticky=W)
student_info_notebook_1.add(general, text='General')
student_info_notebook_1.add(address, text='Address')
student_info_notebook_1.add(contact, text='Contact')
student_info_notebook_2.add(payment, text='Payment')
notes_notebook.add(notes, text='Notes')
portrait_notebook.add(portrait, text='Photo')

''' style '''
tab_style = tkinter.ttk.Style()
tab_style.configure('TNotebook.Tab', font=('Helvetica', 11))

''' widgets '''
first_name = textbox.Textbox(general, 0, 0)
last_name = textbox.Textbox(general, 1, 0)
chinese_name = textbox.Textbox(general, 2, 0)
date_of_birth = date_textbox.Date_textbox(general, 3, 0)
age = textbox.Textbox(general, 4, 0)
card_printed = textbox.Textbox(general, 5, 0)
barcode = textbox.Textbox(payment, 6, 0)
tuition_paid_day = date_textbox.Date_textbox(payment, 7, 0)
total_amount = textbox.Textbox(payment, 8, 0)
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
portrait_ = image.Image_(portrait, 0, 0)

''' widget settings '''
first_name.settings(label='First Name')
last_name.settings(label='Last Name')
chinese_name.settings(label='Chinese Name')
date_of_birth.settings(label='Date of Birth')
age.settings(label='Age')
card_printed.settings(label='Card Printed?')
barcode.settings(label='Barcode')
tuition_paid_day.settings(label='Tuition Paid Day')
total_amount.settings(label='Total Amount')
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
notes_.settings(label='Notes', height=10, entry_width=36)
notes_.entry.config(font='Helvetica 11')
notes_.label.pack_forget()
portrait_.settings(image=student_images + 'null_portrait.jpg', resize=(135, 135))

zipcode.set_input_restriction('int')
home_phone.set_input_restriction('int')
cell_phone_1.set_input_restriction('int')
cell_phone_2.set_input_restriction('int')

''' set fill tags '''