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
	all_rows = [[info_sheet.cell_value(row, i) for i in range(0, info_sheet.ncols)] for row in range(2, num_rows)]

	#column_number_assoc = {col:columns.index(col) for col in columns}

	result = []

	for row in all_rows:
		zipped = list(zip(columns, row))
		student_ = {}
		
		for prop in zipped:
			column_name = prop[0]
			if column_name == 'Date of Birth':
				#convert excel date into datetime
				days = prop[1] if prop[1] > 25569 else 25570
				seconds = (days - 25569) * 86400.0
				dt = datetime.datetime.utcfromtimestamp(seconds)

				student_[column_associations.column_associations[prop[0]]] = dt
			elif column_name in column_associations.column_associations:
				student_[column_associations.column_associations[prop[0]]] = prop[1]

		result.append(student_)


	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	db_editor = db_test.Database_editor()
	db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

	for student_ in result:
		db_editor.add_student(student_)



	#print(column_number_assoc)
	#print(result)
	#print(columns, all_rows)
	return

source = 'C:\\Users\\Bipro\\Documents\\GitHub\\Project-RYB\\controllers\\Student DataBase 3.xls'
convert_database(source, 'test')