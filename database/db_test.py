import sqlite3
import datetime
import shutil


class Database_editor:

	def create_open_database(self, db_filepath, db_templ_filepath=False):
		if db_templ_filepath:
			shutil.copy(db_templ_filepath, db_filepath)
		self.conn = sqlite3.connect(db_filepath)
		self.cur = self.conn.cursor()

	def add_student(self, data_table):
		table_columns = {
			#names of table columns
			'student_info': [row[1] for row in self.cur.execute('PRAGMA table_info(student_info)')],
			'address': [row[1] for row in self.cur.execute('PRAGMA table_info(address)')],
			'contact_info': [row[1] for row in self.cur.execute('PRAGMA table_info(contact_info)')],
			'class_info': [row[1] for row in self.cur.execute('PRAGMA table_info(class_info)')],
			'card': [row[1] for row in self.cur.execute('PRAGMA table_info(card)')],
			'notes': [row[1] for row in self.cur.execute('PRAGMA table_info(notes)')]
		}

		for table_name, table_columns_ in table_columns.items():
			'''
			table_values = create a list ordered by columns from table_columns
			value_fill = (?, ?, ..) tuple converted to string for script
			'''
			table_values = tuple([data_table[column_name] for column_name in table_columns_])
			value_fill = str(tuple(['?' for i in table_columns[table_name]])).replace("'", '')
			script = 'INSERT INTO ' + table_name + ' VALUES ' + value_fill

			self.cur.execute(script, table_values)
			self.conn.commit()

	def fetch_data(self, id):
		'''
		add data from table by id
		match column name and data by
			{column_name: column_data for (column_name, column_data) in zip(table, table_data by id)}
		'''
		data = {}
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(student_info)')], \
				[row for row in self.cur.execute('SELECT * FROM student_info WHERE id=?', (id, ))][0])
			})
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(address)')], \
				[row for row in self.cur.execute('SELECT * FROM address WHERE id=?', (id, ))][0])
			})
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(contact_info)')], \
				[row for row in self.cur.execute('SELECT * FROM contact_info WHERE id=?', (id, ))][0])
			})
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(class_info)')], \
				[row for row in self.cur.execute('SELECT * FROM class_info WHERE id=?', (id, ))][0])
			})
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(card)')], \
				[row for row in self.cur.execute('SELECT * FROM card WHERE id=?', (id, ))][0])
			})
		data.update({
			column: column_data for (column, column_data) in \
			zip([row[1] for row in self.cur.execute('PRAGMA table_info(notes)')], \
				[row for row in self.cur.execute('SELECT * FROM notes WHERE id=?', (id, ))][0])
			})

		return data

	def get_timeslot(self):
		return

	def scan_student(self, barcode, time=False, scan_type='Barcode'):
		return
		
	def search_database(self, barcode, table):
		return



#x = Database_editor()


#x.create_database('test.db')
#data = {}

#x.create_open_database('test2.db', 'student_db_template.db')
#x.create_open_database('test2.db')

#x.add_student(data)

#x.cur.execute("INSERT INTO student_info VALUES (?, ?, ?, ?, ?)", ('BRK-002', 'Zhen', 'Zhou', datetime.datetime.strptime('10/07/1988', "%m/%d/%Y"), '26'))
#'%Y-%m-%d %H:%M:%S'


#x.conn.commit()

#x.conn.close()

#conn = sqlite3.connect('test2.db')

#c = conn.cursor()

#r = [row for row in c.execute('SELECT * FROM student_info')]
#print(r)

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

#conn.close()