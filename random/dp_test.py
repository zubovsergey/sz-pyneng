# -*- coding: utf-8 -*-

import sqlite3
connection = sqlite3.connect('test_db.db')

cursor = connection.cursor()

#cursor.execute("create table switch (mac text not NULL primary key, hostname text, model text, location text)")

query = "INSERT into switch values (?, ?, ?, ?)"

data = [
   		('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
   		('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
   		('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
   		('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

for row in data:
	cursor.execute(query, row)

connection.commit()