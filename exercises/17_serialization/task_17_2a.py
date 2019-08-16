# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import re
from pprint import pprint
import glob
import yaml

sh_cdp_files = glob.glob('sh_cdp*')
#print(sh_cdp_files)


def generate_topology_from_cdp (list_of_files,save_to_filename):

	final_dict = {}

	for files in list_of_files:
		

		with open(files) as f:
			data = f.readlines()


			for line in data:
				match1 = re.search(r'(?P<sid>^.+>|#)', line)
				match2 = re.search(r'(?P<did>\S+) +(?P<lintf>Eth \S+) +\w+ +\S? \S? \S? +\S+ +(?P<rintf>Eth \S+)', line)

				if match1:
					device_id = match1.group('sid').strip('>|#')
					final_dict[device_id] = {}

				elif match2:
					local_intf = match2.group('lintf')
					rdid = match2.group('did')
					remote_intf = match2.group('rintf')


					final_dict[device_id][local_intf] = {}
					final_dict[device_id][local_intf][rdid] = remote_intf

	#return (final_dict)

	with open(save_to_filename, 'w') as dest_f:
		yaml.dump(final_dict, dest_f)
			

pprint(generate_topology_from_cdp(sh_cdp_files, 'topology.yaml'))
#generate_topology_from_cdp(sh_cdp_files, 'cdp_result.txt')