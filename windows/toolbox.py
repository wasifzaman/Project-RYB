import configparser
from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
sys.path.append(os.path.abspath(os.pardir) + '\controllers') #controllers
controllers = os.path.abspath(os.pardir) + '\controllers\\'
images = os.path.abspath(os.pardir) + '\images\\' #image directory

import button
import table
import textbox
import optionmenu

''' root window '''
toolbox = Toplevel()
toolbox.option_add('*Label.Font', 'Helvetica 11')

''' frame initialization '''
menu_frame = Frame(toolbox, bg='#2A2A3D')
import_export = Frame(toolbox, bg='#2A2A3D')
database = Frame(toolbox, bg='#2A2A3D')
database_info = Frame(database)
school = Frame(toolbox, bg='#2A2A3D')
passwords = Frame(toolbox, bg='#2A2A3D')
payment_db = Frame(toolbox, bg='#2A2A3D')

''' frame packing '''
menu_frame.grid(row=0, column=0, sticky=N+S)
Frame(toolbox, bg='#2A2A3D', width=1).grid(row=0, column=1, sticky=N+S)
import_export.grid(row=0, column=2, sticky=N+S)
database_info.grid(row=0, columnspan=2, sticky=E+W)
#database.pack()
#school.pack()
#passwords.pack()
#payment_db.pack()

''' widgets '''
import_export_button = button.Button_(menu_frame, 0, 0)
database_button = button.Button_(menu_frame, 1, 0)
school_button = button.Button_(menu_frame, 2, 0)
passwords_button = button.Button_(menu_frame, 3, 0)
payment_db_button = button.Button_(menu_frame, 4, 0)
import_stu_info_excel = button.Button_(import_export, 0, 0)
import_time_info_excel = button.Button_(import_export, 1, 0)
current_database = textbox.Textbox(database_info, 0, 0)
encryption = optionmenu.Optionmenu(database_info, 1, 0)
encryption_file = textbox.Textbox(database_info, 2, 0)
create_new_db = button.Button_(database, 2, 0)
choose_db = button.Button_(database, 2, 1)
retrieve_enc_key = button.Button_(database, 3, 0)
encrypt_db = button.Button_(database, 3, 1)
convert_py_sql = button.Button_(database, 4, 0)
current_school = textbox.Textbox(school, 0, 0)
ch_school_to = optionmenu.Optionmenu(school, 1, 0)
ch_school = button.Button_(school, 3, 0)
ch_toolbox_pw = button.Button_(passwords, 0, 0)
payment_info = table.Table(payment_db, 0, 0)
print_payment = button.Button_(payment_db, 2, 0)
return_button = button.Button_(menu_frame, 5, 0)

''' bars '''
Frame(database, bg='#C66100', height=5).grid(row=1, columnspan=2, sticky=E+W)
Frame(payment_db, bg='#C66100', height=5).grid(row=1, columnspan=2, sticky=E+W)
Frame(school, bg='#C66100', height=5).grid(row=2, columnspan=2, sticky=E+W)


''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
import_export_button.settings(text='Import/Export', label_bg=label_bg, hover_bg=hover_bg)
database_button.settings(text='DB Management', label_bg=label_bg, hover_bg=hover_bg)
school_button.settings(text='School', label_bg=label_bg, hover_bg=hover_bg)
passwords_button.settings(text='Passwords', label_bg=label_bg, hover_bg=hover_bg)
payment_db_button.settings(text='Payment', label_bg=label_bg, hover_bg=hover_bg)
import_stu_info_excel.settings(text='Import Student Info', label_bg=label_bg, hover_bg=hover_bg)
import_time_info_excel.settings(text='Import Time Info', label_bg=label_bg, hover_bg=hover_bg)
current_database.settings(label='Current Database', entry_state=DISABLED)
encryption.settings(label='System Encryption', add_option=['On', 'Off'], set_option='On', font='Helvetica 11')
encryption_file.settings(label='Encryption File', entry_state=DISABLED)
create_new_db.settings(text='Create Emtpy Database', label_bg=label_bg, hover_bg=hover_bg)
choose_db.settings(text='Change Database', label_bg=label_bg, hover_bg=hover_bg)
retrieve_enc_key.settings(text='Retrieve System Encryption Key', label_bg=label_bg, hover_bg=hover_bg)
encrypt_db.settings(text='Encrypt Database', label_bg=label_bg, hover_bg=hover_bg)
convert_py_sql.settings(text='Create SQL Database', label_bg=label_bg, hover_bg=hover_bg)
current_school.settings(label='Current School')
ch_school_to.settings(label='Change to')
ch_school.settings(text='Change School', label_bg=label_bg, hover_bg=hover_bg)
ch_toolbox_pw.settings(text='Change Toolbox Password', label_bg=label_bg, hover_bg=hover_bg)
print_payment.settings(text='Print Payment', label_bg=label_bg, hover_bg=hover_bg)
return_button.settings(text='Return to\n Main Menu', label_bg=label_bg, hover_bg=hover_bg)

current_database.entry.config(width=50)
encryption_file.entry.config(width=50)
encryption.widget_frame.grid(sticky=W)
encryption.label.config(width=15)
encryption.combobox.config(width=10)
import_export_button.label.config(width=15, height=2)
database_button.label.config(width=15, height=2)
school_button.label.config(width=15, height=2)
passwords_button.label.config(width=15, height=2)
payment_db_button.label.config(width=15, height=2)
return_button.label.config(width=15, height=2)
import_stu_info_excel.label.config(width=30)
import_time_info_excel.label.config(width=30)
create_new_db.label.config(width=30)
choose_db.label.config(width=30)
retrieve_enc_key.label.config(width=30)
encrypt_db.label.config(width=30)
convert_py_sql.label.config(width=30)
ch_school.label.config(width=35)
ch_toolbox_pw.label.config(width=30)
print_payment.label.config(width=30)
current_school.entry.config(width=30)
current_school.widget_frame.grid(sticky=E+W)
ch_school_to.widget_frame.grid(sticky=E+W)
payment_info.widget_frame.config(bg='#2A2A3D')
payment_info.navigate_frame.config(bg='#2A2A3D')
payment_info.first.config(bg='#2A2A3D', fg='white')
payment_info.last.config(bg='#2A2A3D', fg='white')
payment_info.left.config(bg='#2A2A3D', fg='white')
payment_info.right.config(bg='#2A2A3D', fg='white')
payment_info.go_to_button.config(bg='#2A2A3D', fg='white')
payment_info.go_to.config(font='Helvetica 11')

create_new_db.widget_frame.grid(pady=(0, 1), padx=(0, 1))
retrieve_enc_key.widget_frame.grid(pady=(0, 1), padx=(0, 1))
database_button.widget_frame.grid(pady=(0, 1))
school_button.widget_frame.grid(pady=(0, 1))
passwords_button.widget_frame.grid(pady=(0, 1))
import_export_button.widget_frame.grid(pady=(0, 1))
payment_db_button.widget_frame.grid(pady=(0, 1))
payment_info.widget_frame.grid(pady=(0, 5))
import_stu_info_excel.widget_frame.grid(pady=(0, 1))


toolbox.current_window = 'import_export'
def show_window(window_name):
	if toolbox.current_window == window_name: return
	eval(toolbox.current_window).grid_forget()
	toolbox.current_window = window_name
	eval(toolbox.current_window).grid(row=0, column=2, sticky=N+S)
	return

import_export_button.settings(command=lambda: show_window('import_export'))
database_button.settings(command=lambda: show_window('database'))
school_button.settings(command=lambda: show_window('school'))
passwords_button.settings(command=lambda: show_window('passwords'))
payment_db_button.settings(command=lambda: show_window('payment_db'))