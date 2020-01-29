# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
from netmiko import ConnectHandler
import textfsm
import clitable
from pprint import pprint
import yaml

def send_and_parse_show_command(device_dict,command,templates_path):

	with ConnectHandler(**device_dict) as ssh:
		ssh.enable()
		result_output = ssh.send_command(command)
		device_name = ssh.find_prompt()
	attributes = {'Command': 'show ip int brief' , 'Vendor': 'cisco_ios'}
	cli_table = clitable.CliTable('index', templates_path)
	cli_table.ParseCmd(result_output, attributes)
	#print('CLI Table output:\n', cli_table)
	data_rows = [list(row) for row in cli_table]
	header = list(cli_table.header)
	result = []
	for row in data_rows:
		y = dict(zip(header,row))
		result.append(y)
	d1 = {}
	d1[device_name] = result
	
	return d1

if __name__ == '__main__':

	with open ('devices.yaml') as f:
		device_dict = yaml.safe_load(f)
		#pprint(device_dict)

	pprint(send_and_parse_show_command(device_dict[0],'sh ip int br','templates'))