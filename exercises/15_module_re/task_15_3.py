# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
#(?P<nat_type>(?:static|dynamic)) (?P<protocol>(?:tcp|udp)) (?P<ip>(?:\d+\.){3}\d+) (?P<s_port>(?:\d+)) (\S+) (?P<intf>(?:\S+)) (?P<_port>(?:\d+)))

import re
from pprint import pprint

def convert_ios_nat_to_asa (s_file, d_file):

    regex = ('(?P<nat_type>(?:static|dynamic)) '
             '(?P<protocol>(?:tcp|udp)) '
             '(?P<ip>(?:\d+\.){3}\d+) '
             '(?P<s_port>(?:\d+)) (\S+) '
             '(?P<intf>(?:\S+)) '
             '(?P<d_port>(?:\d+))')

    with open(s_file) as src, open(d_file, 'w') as dst:

    	for line in src:
    		match = re.search(regex, line)
    		if match:
    			x = 'object network LOCAL_{}\n host {}\n nat (inside,outside) {} interface {} {} {} {}\n\n'.format(match.group('ip'), match.group('ip'),match.group('nat_type'),match.group('intf'), match.group('protocol'), match.group('s_port'), match.group('d_port'))
    			dst.write (x)
convert_ios_nat_to_asa ('cisco_nat_config.txt', 'result.txt')