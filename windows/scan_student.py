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

''' root window '''
scan_student = Tk()

''' frame initialization '''
search_frame = Frame(scan_student)
student_info_frame_1 = Frame(scan_student)
student_info_frame_2 = Frame(scan_student)
attendance_table_frame = Frame(scan_student)

''' frame packing '''
search_frame.pack()
student_info_frame_1.pack(side=LEFT)
student_info_frame_2.pack(side=LEFT)
attendance_table_frame.pack(side=LEFT)

''' widgets '''
first_name = textbox.Textbox(student_info_frame_1, 0, 0)
last_name = textbox.Textbox(student_info_frame_1, 1, 0)
chinese_name = textbox.Textbox(student_info_frame_1, 2, 0)
dob = date_textbox.Date_textbox(student_info_frame_1, 3, 0)
age = textbox.Textbox(student_info_frame_1, 4, 0)
card_printed = textbox.Textbox(student_info_frame_1, 5, 0)
barcode = textbox.Textbox(student_info_frame_1, 6, 0)
tuition_paid_day = date_textbox.Date_textbox(student_info_frame_1, 7, 0)
total_amount = textbox.Textbox(student_info_frame_1, 8, 0)
amount_owed = textbox.Textbox(student_info_frame_1, 9, 0)
service_type = textbox.Textbox(student_info_frame_1, 10, 0)
classes_awarded = textbox.Textbox(student_info_frame_1, 11, 0)
classes_remaining = textbox.Textbox(student_info_frame_1, 12, 0)
class_time = textbox.Textbox(student_info_frame_1, 13, 0)
address = textbox.Textbox(student_info_frame_2, 0, 0)
city = textbox.Textbox(student_info_frame_2, 1, 0)
state = textbox.Textbox(student_info_frame_2, 2, 0)
zipcode = textbox.Textbox(student_info_frame_2, 3, 0)
email = textbox.Textbox(student_info_frame_2, 4, 0)
parent_name = textbox.Textbox(student_info_frame_2, 5, 0)
pick_up_person = textbox.Textbox(student_info_frame_2, 6, 0)
home_phone = textbox.Textbox(student_info_frame_2, 7, 0)
cell_phone_1 = textbox.Textbox(student_info_frame_2, 8, 0)
cell_phone_2 = textbox.Textbox(student_info_frame_2, 9, 0)
notes = multiline_textbox.Multiline_textbox(student_info_frame_2, 10, 0)
attendance = table.Table(attendance_table_frame, 5, 5)

''' widget settings '''
first_name.settings(label='First Name')
last_name.settings(label='Last Name')
chinese_name.settings(label='Chinese Name')
dob.settings(label='Date of Birth')
age.settings(label='Age')
card_printed.settings(label='Card Printed?')
barcode.settings(label='Barcode')
tuition_paid_day.settings(label='Tuition Paid Day')
total_amount.settings(label='Total Amount')
amount_owed.settings(label='Amount Owed')
service_type.settings(label='Service Type')
classes_awarded.settings(label='Classes Awarded')
classes_remaining.settings(label='Classes Remaining')
class_time.settings(label='Class Time')
address.settings(label='Address')
city.settings(label='City')
state.settings(label='State')
zipcode.settings(label='Zip Code')
email.settings(label='E-mail')
parent_name.settings(label='Parent Name')
pick_up_person.settings(label='Pick Up Person')
home_phone.settings(label='Home Phone')
cell_phone_1.settings(label='Cell Phone 1')
cell_phone_2.settings(label='Cell Phone 2')
notes.settings(label='Notes', height=5, entry_width=20)

zipcode.set_input_restriction('int')
home_phone.set_input_restriction('int')
cell_phone_1.set_input_restriction('int')
cell_phone_2.set_input_restriction('int')

''' set fill tags '''


scan_student.mainloop()