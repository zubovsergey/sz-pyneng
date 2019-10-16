# -*- coding: utf-8 -*-

import sqlite3
from sys import argv 

data = argv[1:]

def connect_to_db(dbname):

	conn = sqlite3.connect(dbname)

	return conn

def get_data(arg):


	query_dict = {
    'vlan': 'select mac, ip, interface from dhcp where vlan = ?',
    'mac': 'select vlan, ip, interface from dhcp where mac = ?',
    'ip': 'select vlan, mac, interface from dhcp where ip = ?',
    'interface': 'select vlan, mac, ip from dhcp where interface = ?'
	}

	keys = query_dict.keys()

	if 0 < len(arg) == 2:
		key, value = data

		if not key in keys:
			print('Enter key from {}'.format(', '.join(keys)))
		else:
			conn = connect_to_db('dhcp_snooping.db')
			conn.row_factory = sqlite3.Row
			print('\nDetailed information for host(s) with', key, value)
			print('-' * 40)

			query = query_dict[key]
			result = conn.execute(query, (value, ))
			for row in result:
				for row_name in row.keys():
					print('{:12}: {}'.format(row_name, row[row_name]))
				print('-' * 40)

	elif 0 < len(arg) != 2:
		print ('Please, enter ONE or NULL arguments')

	else:
		conn = connect_to_db('dhcp_snooping.db')
		query = 'select * from dhcp'
		print('\ndhcp table has these items: ')
		print('{}   {:<16} {:>5} {:<12}'.format('-' * 17, '-' * 16, '-' * 5, '-' * 16))

		result = conn.execute(query)
		#print (result)
		for r in result:
			print ('{}   {:<16} {:>5} {:<12}'.format(r[0], r[1], r[2], r[3]))
		print('{}   {:<16} {:>5} {:<12}'.format('-' * 17, '-' * 16, '-' * 5, '-' * 16))

get_data (data)
