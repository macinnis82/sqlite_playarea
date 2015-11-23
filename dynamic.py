# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 22:09:15 2015

@author: Administrator
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')
cur = con.cursor()

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

 # Drop Tables if they already exist
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("DROP TABLE IF EXISTS weather")
	
 # Create tables
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	
 # Populate Tables with values
cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

 # Take input from user
user_input = raw_input("What city would you like the weather for?")
query = "select * from weather where upper(city) = '{}'".format(str(user_input).upper())
weather = pd.read_sql(query, con)

if weather.empty:
    print('There is no weather information for that city')
else:
    print weather