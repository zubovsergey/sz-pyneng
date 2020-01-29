# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - шаблон TextFSM. Имя файла, в котором находится шаблон
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''

import textfsm
from pprint import pprint

def parse_output_to_dict(template, command_output):
	with open(template) as temp, open(command_output) as out:
		fsm = textfsm.TextFSM(temp)
		output = fsm.ParseText(out.read())

		result = []
		for line in output:
			y = dict(zip(fsm.header, line))
			result.append(y)


	return result


pprint(parse_output_to_dict('templates/sh_ip_int_br.template','output/sh_ip_int_br.txt'))