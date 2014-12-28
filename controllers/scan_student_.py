import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
import db_test
import add_widget_get_
import add_widget_set

''' tag library '''
'''
each tag library corresponds to sqlite table name
each tag corresponds to sqlite database column name
'''

def start_window():
	import scan_student

	student_data, payment_info = {'id': scan_student.barcode}, {'id': scan_student.barcode}

	scan_student.first_name.add_tag(student_data, 'first_name')
	scan_student.last_name.add_tag(student_data, 'last_name')
	scan_student.date_of_birth.add_tag(student_data, 'date_of_birth')
	scan_student.age.add_tag(student_data, 'age')

	scan_student.parent_full_name.add_tag(student_data, 'parent_full_name')
	scan_student.pick_up_person.add_tag(student_data, 'pick_up_person')
	scan_student.home_phone.add_tag(student_data, 'home_phone')
	scan_student.cell_phone_1.add_tag(student_data, 'cell_phone_1')
	scan_student.cell_phone_2.add_tag(student_data, 'cell_phone_2')
	scan_student.email.add_tag(student_data, 'email')

	scan_student.classes_awarded.add_tag(student_data, 'classes_awarded')
	scan_student.classes_remaining.add_tag(student_data, 'classes_remaining')
	scan_student.regular_class_time.add_tag(student_data, 'regular_class_time')

	scan_student.card_printed.add_tag(student_data, 'card_printed')

	scan_student.address_.add_tag(student_data, 'address')
	scan_student.city.add_tag(student_data, 'city')
	scan_student.zipcode.add_tag(student_data, 'zipcode')

	scan_student.notes_.add_tag(student_data, 'notes')

	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	''' data '''
	def get_data_from_lib(lib_name):
		return {col_name: value.get_() for col_name, value in eval(lib_name).items()}

	def scan_student_():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		data = get_data_from_lib('student_data')
		db_editor.scan_student(data)

	''' temp '''
	''' fetch data '''
	def fetch_student():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		data = db_editor.fetch_data(scan_student.search_value.get_())
		for widget_name, widget in student_data.items():
			if widget_name in data:
				#remove this if statement, solidify code
				widget.set(data[widget_name])

		return