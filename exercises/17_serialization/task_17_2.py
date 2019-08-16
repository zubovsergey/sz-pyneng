# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re

sh_cdp_data = open('sh_cdp_n_sw1.txt').read()

def parse_sh_cdp_neighbors (data):

	final_dict = {}

	for line in data.split('\n'):
		match1 = re.search(r'(?P<sid>^.+>|#)', line)
		match2 = re.search(r'(?P<did>\S+) +(?P<lintf>Eth \S+) +\w+ +\S \S \S +\w+ +(?P<rintf>Eth \S+)', line)

		if match1:
			device_id = match1.group('sid').strip('>|#')
			final_dict[device_id] = {}

		elif match2:
			local_intf = match2.group('lintf')
			rdid = match2.group('did')
			remote_intf = match2.group('rintf')

			final_dict[device_id][local_intf] = {}
			final_dict[device_id][local_intf][rdid] = remote_intf

	return (final_dict)

print(parse_sh_cdp_neighbors(sh_cdp_data))