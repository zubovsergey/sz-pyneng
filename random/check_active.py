# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import sqlite3
import re
from pprint import pprint

def check_active (file, db):

#### read db

	conn = sqlite3.connect(db)
	cursor = conn.cursor()

	db_data = []

	for row in cursor.execute('select * from dhcp'):
		db_data.append(row[:-1])

	pprint (db_data)

#### read file

	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

	result = []

	with open(file) as f:
		for row2 in f:
			match = regex.search(row2)
			if match:
				result.append(match.groups())

#### check interseptions

	for line in result:
		if line in db_data:
			print ('!!!')



check_active ('sw1_dhcp_snooping.txt', 'dhcp_snooping.db')