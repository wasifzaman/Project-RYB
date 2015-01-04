import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
from tkinter import filedialog
from imp import reload
import db_test
import convert_xlsx_to_db
import add_widget_get_
import add_widget_set

def start_window():
	import import_from_xlsx

	if not hasattr(import_from_xlsx, 'load_state'):
		setattr(import_from_xlsx, 'load_state', True)
	else:
		reload(import_from_xlsx)
	
	''' tag library '''
	'''
	each tag library corresponds to sqlite table name
	each tag corresponds to sqlite database column name
	'''

	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	def convert_to_db():
		source = import_from_xlsx.import_xlsx_path.get_()
		destination = import_from_xlsx.destination_path.get_()

		convert_xlsx_to_db.convert_database(source, destination)
		return

	import_from_xlsx.import_browse_button.settings(\
		command=lambda: import_from_xlsx.import_xlsx_path.set(filedialog.askopenfile().name))
	import_from_xlsx.time_browse_button.settings(\
		command=lambda: import_from_xlsx.time_xlsx_path.set(filedialog.askopenfile().name))
	import_from_xlsx.destination_browse_button.settings(\
		command=lambda: import_from_xlsx.destination_path.set(filedialog.asksaveasfilename()))
	import_from_xlsx.cancel_button.settings(command=import_from_xlsx.import_from_xlsx.destroy)
	import_from_xlsx.import_button.settings(command=convert_to_db)


	import_from_xlsx.import_from_xlsx.mainloop()

start_window()