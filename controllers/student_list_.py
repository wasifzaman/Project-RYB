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
	import student_list

	if not hasattr(student_list, 'load_state'):
		setattr(student_list, 'load_state', True)
	else:
		reload(student_list)
	
	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	''' data '''
	def get_data_from_lib(lib_name):
		return {col_name: value.get_() for col_name, value in eval(lib_name).items()}

	def student_list_():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		data = get_data_from_lib('student_data')
		db_editor.student_list(data)

	''' temp '''
	''' fetch data '''
	def fetch_student():
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		data = db_editor.fetch_data('BRK-001')
		for widget_name, widget in student_data.items():
			if widget_name in data:
				#remove this if statement, solidify code
				widget.set(data[widget_name])

		return