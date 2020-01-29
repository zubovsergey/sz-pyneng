# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint

def generate_config(template, data_dict):
	env = Environment(
		loader=FileSystemLoader('templates'),
		trim_blocks=True,
		lstrip_blocks=True)
	temp = env.get_template(template)

	with open(data_dict) as f:
		config = yaml.safe_load(f)
		pprint (config)

	result = temp.render(config)
	
	return result

print(generate_config('for.txt', 'data_files/for.yml'))