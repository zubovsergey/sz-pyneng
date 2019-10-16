# -*- coding: utf-8 -*-

import sqlite3
import os.path
from os import path


def create_connections(db_file):
	"""create a database connection & check if database is already exist"""

	path.exists(db_file) == True

	if path.exists(db_file):
		print ('database is already exist')
	else:
		try:
			conn = sqlite3.connect(db_file)
			print('Creating schema...')
			with open('dhcp_snooping_schema.sql', 'r') as f:
				schema = f.read()
				conn.executescript(schema)
			print ('Done')
		except sqlite3.OperationalError as e:
			print(e)
		finally:
			if conn:
				conn.close()

if __name__ == '__main__':
	create_connections('dhcp_snooping.db')

