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
