import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
from imp import reload
import db_test
import student_set
import add_widget_get_
import add_widget_set
import add_payment_

''' tag library '''
'''
each tag library corresponds to sqlite table name
each tag corresponds to sqlite database column name
'''

def start_window():
	import scan_student

	if not hasattr(scan_student, 'load_state'):
		setattr(scan_student, 'load_state', True)
	else:
		reload(scan_student)

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

	''' fetch data '''
	def fetch_student(id=False):
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		if len(scan_student.search_value.get_()) == 0: return #prevent blank ids
		data = db_editor.fetch_data(id if id else scan_student.search_value.get_())
		for widget_name, widget in student_data.items():
			if widget_name in data:
				#remove this if statement, solidify code
				widget.set(data[widget_name])

		attendance_data_set = db_editor.get_attendance(id)
		for attendance_data in attendance_data_set:
			scan_student.attendance_table.settings(add_row=attendance_data)

		return

	def fetch_student_set():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		column_name = {
			'First Name': 'first_name',
			'Last Name': 'last_name'
		}

		ordered_columns = ['id', 'first_name', 'last_name', 'chinese_name', 'date_of_birth'] #column order of table
		data = db_editor.fetch_id_set(scan_student.search_value.get_(), column_name[scan_student.search_type.stringvar.get()])
		if len(data) == 1:
			fetch_student(data[0]['id'])
		elif len(data) > 1:
			#order columns and pass it to student_set
			ordered_data = [[student[column_name_] for column_name_ in ordered_columns] for student in data]
			student_set.start_window(ordered_data)

	def create_payment():
		if len(scan_student.barcode.get_()) == 0: return #prevent blank ids

		add_payment_.start_window(scan_student.barcode.get_())



	scan_student.search_button.settings(command=lambda: fetch_student_set() if scan_student.search_type.stringvar.get() != 'Barcode' else fetch_student(scan_student.search_value.get_()))
	scan_student.create_payment.settings(command=lambda: create_payment())