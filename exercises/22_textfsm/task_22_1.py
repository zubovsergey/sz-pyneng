# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - шаблон TextFSM. Имя файла, в котором находится шаблон
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''
import textfsm
from pprint import pprint

def parse_command_output(template, command_output):
	with open(template) as t, open(command_output) as r:
		fsm = textfsm.TextFSM(t)
		result = fsm.ParseText(r.read())

	return fsm.header, result


pprint(parse_command_output('templates/sh_ip_int_br.template','output/sh_ip_int_br.txt'))