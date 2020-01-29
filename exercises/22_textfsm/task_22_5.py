# -*- coding: utf-8 -*-
'''
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
'''

from netmiko import ConnectHandler
import textfsm
import clitable
from pprint import pprint
import yaml

from concurrent.futures import ThreadPoolExecutor, as_completed
from task_22_4	import send_and_parse_show_command

def send_and_parse_command_parallel(devices, command, templates_path, limit):
	data = []
	with ThreadPoolExecutor(max_workers=limit) as executor:
		futures=[]
		for device in devices:
			futures.append(executor.submit(send_and_parse_show_command, device, command, templates_path))

		for f in as_completed(futures):
			data.append(f.result())
	
	return data

if __name__ == '__main__':
	with open ('devices.yaml') as f:
		device_dict = yaml.safe_load(f)

pprint(send_and_parse_command_parallel(device_dict, 'sh ip int br', 'templates', 3))