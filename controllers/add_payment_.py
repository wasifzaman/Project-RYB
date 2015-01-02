import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\windows') #windows directory
sys.path.append(os.path.abspath(os.pardir) + '\database') #windows directory

from tkinter import *
from imp import reload
import db_test
import student_set
import add_widget_get_
import add_widget_set

''' tag library '''
'''
each tag library corresponds to sqlite table name
each tag corresponds to sqlite database column name
'''

def start_window(id):
	import add_payment

	if not hasattr(add_payment, 'load_state'):
		setattr(add_payment, 'load_state', True)
	else:
		reload(add_payment)

	print(id)