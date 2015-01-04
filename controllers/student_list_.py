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
import edit_student_

def start_window():
	import student_list

	if not hasattr(student_list, 'load_state'):
		setattr(student_list, 'load_state', True)
	else:
		reload(student_list)

	student_list.student_table.settings(add_row=['Barcode', 'First Name', 'Last Name', 'Chinese Name', 'Date of Birth'])
	
	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	''' data '''
	def get_data_from_lib(lib_name):
		return {col_name: value.get_() for col_name, value in eval(lib_name).items()}

	def fetch_all_student():
		def bind_single_edit_student(label_, id):
			label_.bind('<Double-Button-1>', lambda event: edit_student_.start_window(id))
			return

		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		rows = db_editor.fetch_all_student()
		for row in rows:
			student_list.student_table.settings(add_row=row)
			for label in student_list.student_table.rows[-1]:
				bind_single_edit_student(label, row[0])

		return

	fetch_all_student()