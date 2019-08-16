# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла, в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''
import re
from pprint import pprint
import glob
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'uptime', 'image']


def parse_sh_version(data_sh_ver):
	
	data_result = []

	for line in data_sh_ver:

		if 'Cisco IOS' in line:
			match = re.search('Version (?P<osver>(?:\S+))', line)
			ios = match.group('osver').strip(',')
			data_result.append(ios)
		elif 'System image file is' in line:
			match2 = re.search('System image file is (?P<img>(?:\S+))',line)
			image = match2.group('img').strip('"')
			data_result.append(image)
		elif 'uptime' in line:
			match3 = re.search('router uptime is (?P<upt>(?:\S+) ?\S+ ?\S+ ?\S+ ?\S+ ?\S+)', line)
			uptime = match3.group('upt').strip()
			data_result.append(uptime)		


	return data_result


def write_inventory_to_csv(data_filenames, csv_filename):

	final_result = [headers]

	for files in data_filenames:

		result = []
		result.append(files.split('.')[0].split('_')[-1])
		

		with open (files, 'r') as f:
			data = f.readlines()
			#print (x)
			for i in parse_sh_version(data):
				result.append(i)


		final_result.append(result)

	#print (final_result)

	with open(csv_filename, 'w') as dest:
		writer = csv.writer(dest, quoting=csv.QUOTE_NONNUMERIC)

		for row in final_result:
				writer.writerow(row)



write_inventory_to_csv(sh_version_files, 'result_sh_version.csv')

