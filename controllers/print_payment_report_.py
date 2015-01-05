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
import print_reports

def start_window():
	import print_payment_report

	if not hasattr(print_payment_report, 'load_state'):
		setattr(print_payment_report, 'load_state', True)
	else:
		reload(print_payment_report)

	def set_output_folder():
		output = filedialog.askdirectory()
		print_payment_report.output_folder.set(output)

	def print_date_report():
		start_dt = print_payment_report.start_date.get_()
		end_dt = print_payment_report.end_date.get_()
		print_reports.print_payment_report(start_dt, end_dt, print_payment_report.output_folder.get_())
		print_payment_report.print_payment_report.destroy()

	print_payment_report.browse_output_folder.settings(command=set_output_folder)
	print_payment_report.confirm_button.settings(command=print_date_report)
	print_payment_report.cancel_button.settings(command=print_payment_report.print_payment_report.destroy)