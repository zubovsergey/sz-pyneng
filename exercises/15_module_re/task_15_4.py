# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re
from pprint import pprint


def get_ints_without_description (file):

    result = {}
    with open(file) as f:
        for line in f:
            line = line.rstrip()

            if line and not ('!') in line:
                if line[0].isalnum():
                    level_1 = line
                    result[level_1] = []
                elif line.startswith(' ') and line[1].isalnum():
                    last_level_2 = line
                    result[level_1].append(line)
                else:
                    #если команда 3 уровня встретилась первый раз,
                    #результатом будет список
                    if type(result[level_1]) is list:
                        result[level_1] = {key:[] for key in result[level_1]}
                    result[level_1][last_level_2].append(line)

 
    result2 = {}

    for key, value in result.items():
    	if 'interface ' in str(key):	
    		#result2[key] = None
    		if 'description' not in str(value):
    			result2[key] = value

    pprint (result2)

get_ints_without_description ('config_r1.txt')
#pprint(get_ints_without_description ('config_r1.txt'))