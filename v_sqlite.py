import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data = cur.fetchone()
	print("SQLITE_VERSION: %s" % data)