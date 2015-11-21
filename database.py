import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

cities = (
	('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'),
    ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'),
    ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA'),
	('Washington', 'DC'), ('Houston', 'TX'),  ('Las Vegas', 'NV'), 
	('Atlanta', 'GA')
)

weather = (
	('New York City', 2013, 'July', 'January', 62),
	('Boston', 2013, 'July', 'January', 59),
	('Chicago', 2013, 'July', 'January', 59),
	('Miami', 2013, 'August', 'January', 84),
	('Dallas', 2013, 'July', 'January', 77),
	('Seattle', 2013, 'July', 'January', 61),
	('Portland', 2013, 'July', 'December', 63),
	('San Francisco', 2013, 'September', 'December', 64),
	('Los Angeles', 2013, 'September', 'December', 75),
	('Washington', 2013, 'July', 'January', 59),
	('Houston', 2013, 'July', 'January', 62),
	('Las Vegas', 2013, 'July', 'December', 83),
	('Atlanta', 2013, 'July', 'January', 51)
)

with con:
	cur = con.cursor()
	
	# Drop Tables if they already exist
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	
	# Create tables
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	
	# Populate Tables with values
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	
	# Query the tables
	cur.execute("SELECT name, state from cities inner join weather on name=city where warm_month='July'")
	
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	
	for row in df.iterrows():
		index, data = row
		print 'The cities that are the warmest in July are: %s, %s' % (data['name'], data['state'])
	#print("The cities that are the warmest in July are: {}, {}".format(df['name'], df['state']))