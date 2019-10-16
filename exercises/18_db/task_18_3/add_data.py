# -*- coding: utf-8 -*-

import sqlite3
import os.path
from os import path
import re
import yaml
from pprint import pprint
import glob

dhcp_snooping_files = glob.glob('sw*dhcp_snooping*')

def add_data_to_tables (switches_filename, dhcp_filenames, db_filename):

	conn = sqlite3.connect(db_filename)
	print('Inserting DHCP Snooping data')

	with open (switches_filename) as fs:
		switches = yaml.safe_load(fs)

		for v in switches.values():
			for v2 in v.items():
				try:
					with conn:
						query = '''insert into switches (hostname, location) 
									values (?, ?)'''
						conn.execute(query, v2)
				except sqlite3.IntegrityError as e:
					print('Adding {} Error occured: '.format(v2), e)

		for files in dhcp_filenames:

			regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

			result = []
			
			with open(files) as f: 
				for line in f:
					match = regex.search(line)
					if match:
						result.append(match.groups() + tuple('1'))
		
			name_regex = re.compile('(sw\d+)')
			match2 = name_regex.search(files)

			if match2:
				name = tuple(match2.groups())


			###pprint (result)	
	
			for row in result:
				try:
					with conn:
						query = '''insert into dhcp (mac, ip, vlan, interface, active, switch)
									values (?, ?, ?, ?, ?, ?)'''
						conn.execute(query, row + name)
				except sqlite3.IntegrityError as e:
					print('Adding {} Error occured: '.format(row + name), e)
	
	conn.close()	


if __name__ == '__main__':
	add_data_to_tables('switches.yml', dhcp_snooping_files, 'dhcp_snooping.db')