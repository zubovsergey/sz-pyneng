# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import textfsm
import clitable
from pprint import pprint

attributes = {'Command': 'show ip int brief' , 'Vendor': 'cisco_ios'}

def parse_command_dynamic (command_output,attributes_dict,index_file,templ_path):
	with open(command_output) as f:
		output_sh_ip_int_br = f.read()

	attributes = attributes_dict

	cli_table = clitable.CliTable(index_file, templ_path)

	cli_table.ParseCmd(output_sh_ip_int_br, attributes)
	#print('CLI Table output:\n', cli_table)

	#print('Formatted Table:\n', cli_table.FormattedTable())

	data_rows = [list(row) for row in cli_table]
	header = list(cli_table.header)
	#print(header)
	#print (data_rows)
	
	result = []
	for row in data_rows:
		y = dict(zip(header,row))
		result.append(y)
	
	return result

pprint(parse_command_dynamic('output/sh_ip_int_br.txt',attributes,'index','templates'))