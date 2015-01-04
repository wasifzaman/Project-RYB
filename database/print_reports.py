import configparser
import os, sys
controllers = os.path.abspath(os.pardir) + '\controllers\\' #controller directory

import db_test
import datetime
import xlsxwriter

def print_date_report(check_in_date, output_folder):
	''' config file '''
	config = configparser.ConfigParser()
	config.read(controllers + 'config.ini', encoding='utf-8')

	db_editor = db_test.Database_editor()
	db_editor.create_open_database(config['DEFAULT']['DBFILEPATH'])

	rows = [row for row in db_editor.cur.execute('SELECT * FROM attendance_table')]
	result = []

	for row in rows:
		date = datetime.datetime.strptime(row[2][:10], '%Y-%m-%d')
		if date == check_in_date:
			result.append(row)

	today = datetime.datetime.now()
	date = today.strftime('%m.%d.%y')
	time = today.strftime('%I.%M.%p')
	print(date, time)

	workbook = xlsxwriter.Workbook(output_folder + '/Student Report - ' + 'Test School' + ' ' + date + ' ' + time + '.xlsx')
	worksheet = workbook.add_worksheet()

	worksheet.write(0, 0, 'Barcode')
	worksheet.write(0, 1, 'Scan Time')
	worksheet.write(0, 2, 'Class Time')
	worksheet.write(0, 3, 'Scan Type')

	r = 1
	for row in result:
		scan_time = datetime.datetime.strftime(datetime.datetime.strptime(row[1][11:16], '%H:%M'), '%I:%M %p')
		class_time = datetime.datetime.strftime(datetime.datetime.strptime(row[2][11:16], '%H:%M'), '%I:%M %p')
		worksheet.write(r, 0, row[0])
		worksheet.write(r, 1, scan_time)
		worksheet.write(r, 2, class_time)
		worksheet.write(r, 3, row[3])
		r += 1

	return True

#out_folder = 'C:\\Users\\Bipro\\Desktop\\'
#dt = datetime.datetime(2015, 1, 1)
#print_date_report(dt, out_folder)