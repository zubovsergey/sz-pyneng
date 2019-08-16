# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
from pprint import pprint

def get_ip_from_cfg (filename):

	with open(filename, 'r') as f:

		result = {}
		x = []

		for line in f:
			if line.startswith('interface'):
				intf = re.search('interface (\S+)', line).group()
				#result[intf]={}
			elif "ip address" in line:
				match = re.search('(?P<ip>(?:\d+\.){3}\d+) (?P<mask>(?:\d+\.){3}\d+)', line)
				if match:
					result[intf]=match.groups()

		return result


pprint(get_ip_from_cfg('config_r1.txt'))