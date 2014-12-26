import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory

import db_test
from add_student import *

''' tag library '''
'''
each tag library corresponds to sqlite table name
each tag corresponds to sqlite database column name
'''

student_data, payment_info = {'id': barcode}, {'id': barcode}

first_name.add_tag(student_data, 'first_name')
last_name.add_tag(student_data, 'last_name')
date_of_birth.add_tag(student_data, 'date_of_birth')
age.add_tag(student_data, 'age')

parent_full_name.add_tag(student_data, 'parent_full_name')
pick_up_person.add_tag(student_data, 'pick_up_person')
home_phone.add_tag(student_data, 'home_phone')
cell_phone_1.add_tag(student_data, 'cell_phone_1')
cell_phone_2.add_tag(student_data, 'cell_phone_2')

classes_awarded.add_tag(student_data, 'classes_awarded')
classes_remaining.add_tag(student_data, 'classes_remaining')
regular_class_time.add_tag(student_data, 'regular_class_time')

card_printed.add_tag(student_data, 'card_printed')

address_.add_tag(student_data, 'address')
city.add_tag(student_data, 'city')
zipcode.add_tag(student_data, 'zipcode')

''' config file '''
config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT']['DBFILEPATH'])

''' data '''
def get_data_from_lib(lib_name):
	return {col_name: value.get_() for col_name, value in eval(lib_name).items()}

def add_student_():
	db_editor = db_test.Database_editor()
	db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

	data = get_data_from_lib('student_data')
	db_editor.add_student(data)

Button(add_student, text='Add Student', command=add_student_).pack()

add_student.mainloop()