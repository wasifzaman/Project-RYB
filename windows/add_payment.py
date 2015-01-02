from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory

import button
import textbox
import date_textbox
import optionmenu

''' root '''
add_payment = Toplevel()
add_payment.option_add('*Label.Font', 'Helvetica 11')
add_payment.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
payment_frame = Frame(add_payment)#, bg='#2A2A3D')
payment_type_frame = Frame(payment_frame)
button_frame = Frame(add_payment, bg='#2A2A3D')
button_container_frame = Frame(button_frame, bg='#2A2A3D')

''' frame packing '''
payment_frame.pack(fill=X)
Frame(add_payment, bg='#C66100', height=5).pack(fill=X)
button_frame.pack(fill=X)
button_container_frame.pack()
payment_type_frame.grid(row=2, columnspan=2)

''' widgets '''
tuition_pay_day = date_textbox.Date_textbox(payment_frame, 0, 0)
payment_type = optionmenu.Optionmenu(payment_type_frame, 0, 0)
check_number = textbox.Textbox(payment_type_frame, 1, 0)
total_amount = textbox.Textbox(payment_frame, 4, 0)
already_paid = textbox.Textbox(payment_frame, 5, 0)
amount_owed = textbox.Textbox(payment_frame, 6, 0)
cancel_button = button.Button_(button_container_frame, 0, 0)
add_payment_button = button.Button_(button_container_frame, 0, 1)
new_balance = Label(payment_frame, text='New Balance', bg='orange')
new_balance.grid(row=3, columnspan=2, sticky=E+W, ipady=1)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
tuition_pay_day.settings(label='Tuition Pay Day')
payment_type.settings(label='Payment Type', add_option=['Cash', 'Check'], set_option='Cash', font='Helvetica 11')
check_number.settings(label='Check Number')
total_amount.settings(label='Total Amount')
already_paid.settings(label='Already Paid')
amount_owed.settings(label='Amount Owed')
cancel_button.settings(text='Cancel', label_bg=label_bg, hover_bg=hover_bg)
add_payment_button.settings(text='Add', label_bg=label_bg, hover_bg=hover_bg)