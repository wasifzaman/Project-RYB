import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
from imp import reload
import db_test
import add_widget_get_
import add_widget_set

def start_window():
	import add_student

	if not hasattr(add_student, 'load_state'):
		setattr(add_student, 'load_state', True)
	else:
		reload(add_student)
	
	''' tag library '''
	'''
	each tag library corresponds to sqlite table name
	each tag corresponds to sqlite database column name
	'''

	student_data, payment_info = {'id': add_student.barcode}, {'id': add_student.barcode}

	add_student.first_name.add_tag(student_data, 'first_name')
	add_student.last_name.add_tag(student_data, 'last_name')
	add_student.chinese_name.add_tag(student_data, 'chinese_name')
	add_student.date_of_birth.add_tag(student_data, 'date_of_birth')
	add_student.age.add_tag(student_data, 'age')
	add_student.gender.add_tag(student_data, 'gender')

	add_student.parent_full_name.add_tag(student_data, 'parent_full_name')
	add_student.pick_up_person.add_tag(student_data, 'pick_up_person')
	add_student.home_phone.add_tag(student_data, 'home_phone')
	add_student.cell_phone_1.add_tag(student_data, 'cell_phone_1')
	add_student.cell_phone_2.add_tag(student_data, 'cell_phone_2')
	add_student.email.add_tag(student_data, 'email')

	add_student.classes_awarded.add_tag(student_data, 'classes_awarded')
	add_student.classes_remaining.add_tag(student_data, 'classes_remaining')
	add_student.regular_class_time.add_tag(student_data, 'regular_class_time')

	add_student.card_printed.add_tag(student_data, 'card_printed')

	add_student.address_.add_tag(student_data, 'address')
	add_student.city.add_tag(student_data, 'city')
	add_student.state.add_tag(student_data, 'state')
	add_student.zipcode.add_tag(student_data, 'zipcode')

	add_student.notes_.add_tag(student_data, 'notes')

	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	''' data '''
	def get_data_from_lib(lib_name):
		return {col_name: value.get_() for col_name, value in lib_name.items()}

	def add_student_():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		data = get_data_from_lib(student_data)
		db_editor.add_student(data)

	add_student.add_button.settings(command=add_student_)
	add_student.return_button.settings(command=add_student.add_student.destroy)