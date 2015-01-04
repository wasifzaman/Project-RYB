import configparser
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

import db_test
import datetime
import xlrd
import column_associations

def convert_database(source_path, dest_path):
	workbook = xlrd.open_workbook(source_path)

	info_sheet = workbook.sheet_by_index(0)
	num_rows = info_sheet.nrows

	columns = [info_sheet.cell_value(0, i) for i in range(0, info_sheet.ncols)]
	all_rows = [[(info_sheet.cell_value(row, i),info_sheet.cell_type(row, i)) for i in range(0, info_sheet.ncols)] for row in range(2, num_rows)]

	result = []
	payment_info = []

	for row in all_rows:
		zipped = list(zip(columns, row))
		student_ = {}
		payment_ = {
			'date': '',
			'total': '',
			'already_paid': '',
			'amount_owed': '',
			'payment_type': '',
			'check_number': '',
		}

		for prop in zipped:
			value = prop[1][0]
			cell_type = prop[1][1]
			column_name = prop[0]

			if column_name in column_associations.info_columns:
				if cell_type == 3:
					#cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blan
					#convert excel date into datetime
					days = value if value > 25569 else 25570
					seconds = (days - 25569) * 86400.0
					value = datetime.datetime.utcfromtimestamp(seconds)
				student_[column_associations.info_columns[column_name]] = value

			if column_name in column_associations.payment_columns:
				if cell_type == 3:
					days = value if value > 25569 else 25570
					seconds = (days - 25569) * 86400.0
					value = datetime.datetime.utcfromtimestamp(seconds)
				payment_[column_associations.payment_columns[column_name]] = value

		result.append(student_)
		payment_info.append(payment_)


	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	db_editor = db_test.Database_editor()
	db_editor.create_open_database(dest_path, config['DEFAULT']['TEMPLATEPATH'])
	#db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

	for student_ in result:
		db_editor.add_student(student_)

	for payment in payment_info:
		db_editor.add_new_payment(payment['id'], payment)

	return True

#source = 'C:\\Users\\Bipro\\Documents\\GitHub\\Project-RYB\\controllers\\Student DataBase 3.xls'
#convert_database(source, 'C:\\users\\bipro\\desktop\\test5.db')