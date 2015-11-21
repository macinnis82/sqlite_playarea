import sqlite3 as lite

cities = ( ('Las Vegas', 'NV'), ('Atlanta', 'GA') )

weather = ( ('Las Vegas', 2013, 'July', 'December', 83), ('Atlanta', 2013, 'July', 'January', 51) )

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)