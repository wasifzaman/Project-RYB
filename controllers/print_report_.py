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
	import print_report

	if not hasattr(print_report, 'load_state'):
		setattr(print_report, 'load_state', True)
	else:
		reload(print_report)

	def set_output_folder():
		output = filedialog.askdirectory()
		print_report.output_folder.set(output)

	def print_date_report():
		dt = print_report.print_date.get_()
		print_reports.print_date_report(dt, print_report.output_folder.get_())
		print_report.print_report.destroy()

	print_report.browse_output_folder.settings(command=set_output_folder)
	print_report.confirm_button.settings(command=print_date_report)
	print_report.cancel_button.settings(command=print_report.print_report.destroy)