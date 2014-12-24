import sqlite3
import datetime



class Database_editor:

	def create_database(self, db_filepath):
		self.conn = sqlite3.connect(db_filepath)
		self.cur = self.conn.cursor()
		self.cur.execute('''
			CREATE TABLE student_info
				(barcode text unique, first_name text, last_name text, chinese_name text, dob text, age real, card_printed integer,
					address text, city text, state text, zip integer, email text,
					parent_name text, pick_up_person text, home_phone integer, cell_phone1 integer, cell_phone2 integer,
					notes text)
			''')
		self.cur.execute('''
			CREATE TABLE attendance
				(barcode text unique, check_in_date text, check_in_time text, class_time text, scan_type text)
			''')
		self.cur.execute('''
			CREATE TABLE payment
				(barcode text unique, tuition_pay_date text, total_paid real, amount_owed real, service_type text, classes_awarded integer, classes_remaining integer, regular_class_time text)
			''')
		self.conn.commit()
		self.conn.close()

	def open_database(self, db_filepath):
		self.conn = sqlite3.connect(db_filepath)
		self.cur = self.conn.cursor()

	def add_student(self, data):
		columns = [column for column in self.cur.execute('PRAGMA table_info(student_info)')]
		ordered_columns = tuple([key[1] for key in columns])
		filled_values = tuple([data[key] for key in ordered_columns])
		script = 'INSERT INTO student_info ' + str(ordered_columns) + ' values ' + str(filled_values)
		self.cur.execute(script)
		self.conn.commit()

	def get_timeslot(self):
		return

	def scan_student(self, barcode, time=False, scan_type='Barcode'):
		scan = (str(barcode, datetime.now().date, datetime.now().time, datetime.now().time, scan_type), )
		self.cur.execute('INSERT INTO attendance VALUES symbol=?', scan)

	def search_database(self, barcode, table):
		barcode = (barcode, )
		script = 'SELECT * FROM ' + table + ' WHERE barcode=?'
		x.cur.execute(script, barcode)
		
		return x.cur.fetchone()




x = Database_editor()

#x.create_database('test.db')
data = {'barcode': 'asdw2', 'first_name': 'a', 'last_name': 'b', 'chinese_name': 'c', 'dob': 'd', 'age': 'e', 'card_printed': 'f',
		'address': 'a', 'city': 'b', 'state': 'c', 'zip': 'd', 'email': 'e',
		'parent_name': 'a', 'pick_up_person': 'b', 'home_phone': 'c', 'cell_phone1': 'd', 'cell_phone2': 'e',
		'notes': ''}

x.open_database('test.db')
#x.add_student(data)

#barcode = (1234, )
#x.cur.execute('SELECT * FROM general_info WHERE barcode=?', barcode)
#row = x.cur.fetchone()
#print(row)
	
all_ = x.search_database('asdw2', 'student_info')
print(all_)














conn = sqlite3.connect('test2.db')

c = conn.cursor()

#c.execute('''
#		CREATE TABLE student_info
 #            (first_name text, last_name text, dob date)
#	''')

#c.execute("INSERT INTO student_info VALUES ('BRK-002', 'Zhen','Zhou', '1988-06-25', 26)")
#c.execute("INSERT INTO student_info VALUES ('Aasif','Zaman', '1988/10/07')")
#c.execute("INSERT INTO student_info VALUES ('Zasif','Zaman', '1988/10/07')")

#conn.commit()

#conn.close()



#c.execute('''
#		UPDATE student_info
#		SET first_name='ZED'
#		WHERE first_name='Wasif'
#	''')


#r = [row for row in c.execute('SELECT * FROM student_info ORDER BY first_name')]
#print(r)


#r = [column for column in c.execute('''
#	PRAGMA table_info(student_info)
#	''')]

#print(r)

conn.close()