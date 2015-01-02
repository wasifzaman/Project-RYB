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

	class return_:
		pass

	widget_ = return_()
	widget_.values = {
		'date': '',
		'total': '',
		'already_paid': '',
		'amount_owed': '',
		'payment_type': '',
		'check_number': ''
	}

	def set_return_values(state):
		if not state:
			widget_.values = False
		elif state:
			widget_.values['date'] = add_payment.tuition_pay_day.get_()
			widget_.values['total'] = add_payment.total_amount.get_()
			widget_.values['already_paid'] = add_payment.already_paid.get_()
			widget_.values['amount_owed'] = add_payment.amount_owed.get_()
			widget_.values['payment_type'] = add_payment.payment_type.stringvar.get()
			widget_.values['check_number'] = add_payment.check_number.get_()

		add_payment.add_payment.destroy()



	add_payment.add_payment_button.settings(command=lambda: set_return_values(True))
	add_payment.cancel_button.settings(command=lambda: set_return_values(False))


	add_payment.add_payment.wait_window()


	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	if widget_.values:
		db_editor = db_test.Database_editor()
		db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

		db_editor.add_new_payment(id, widget_.values)

	print(widget_.values)