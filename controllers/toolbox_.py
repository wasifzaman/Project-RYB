import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

from tkinter import *
from tkinter import filedialog
from imp import reload
import db_test
import add_widget_get_
import add_widget_set
import import_from_xlsx_

def start_window():
	import toolbox

	if not hasattr(toolbox, 'load_state'):
		setattr(toolbox, 'load_state', True)
	else:
		reload(toolbox)
	
	''' tag library '''
	'''
	each tag library corresponds to sqlite table name
	each tag corresponds to sqlite database column name
	'''

	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	db_editor = db_test.Database_editor()
	db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

	def change_school():
		new_school = toolbox.ch_school_to.stringvar.get()
		db_editor.change_school(new_school)
		toolbox.current_school.settings(entry=db_editor.get_school())

	def change_db():
		new_db = filedialog.askopenfilename()
		#config['DEFAULT']['DBFILEPATH'] = new_db
		config.set('DEFAULT', 'DBFILEPATH', new_db)
		with open(controllers + 'config.ini', 'w') as configfile:
			config.write(configfile)
		toolbox.current_database.set(new_db)

	toolbox.current_school.settings(entry=db_editor.get_school())
	toolbox.current_database.settings(entry=config['DEFAULT']['DBFILEPATH'])
	toolbox.ch_school_to.settings(\
		add_option=config['DEFAULT']['SCHOOLS'].split(','),\
		set_option=config['DEFAULT']['SCHOOLS'].split(',')[0],\
		font='Helvetica 11')
	toolbox.ch_school.settings(command=change_school)
	toolbox.import_from_xlsx.settings(command=import_from_xlsx_.start_window)
	toolbox.create_new_db.settings(\
		command=lambda: db_editor.create_open_database(\
			filedialog.asksaveasfilename() + '.db',\
			config['DEFAULT']['TEMPLATEPATH']))
	toolbox.change_db.settings(command=change_db)