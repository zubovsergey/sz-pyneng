# -*- coding: utf-8 -*-

import sqlite3
from pprint import pprint

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]


def create_connection(db_name):
    '''
    Функция создает соединение с БД db_name
    и возвращает его
    '''
    connection = sqlite3.connect(db_name)
    return connection


def write_data_to_db(connection, query, data):

	try:
		with connection:
			connection.executemany(query, data)
	except sqlite3.IntegrityError as e:
		print('Error occured: ', e)
		return False
	else:
		print('Запись данных прошла успешно')
		return True


def get_all_from_db(connection, query):

	result = [row for row in connection.execute(query)]
	return result


if __name__ == '__main__':
    con = create_connection('sw_inventory3.db')

    print('Creating table...')
    schema = '''create table switch
                (mac text primary key, hostname text, model text, location text)'''
    
    #con.execute(schema)

    query_insert = 'INSERT into switch values (?, ?, ?, ?)'
    query_get_all = 'SELECT * from switch'

    print('writing to database:')
    pprint(data)
    write_data_to_db(con, query_insert, data)
    print('\nchecking database:')
    pprint(get_all_from_db(con, query_get_all))

    con.close()
