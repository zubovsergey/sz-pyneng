# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''

import subprocess
import ipaddress
from tabulate import tabulate


def check_ip_availability(line):

    ip = []

    for lines in line:
        ips = lines.split('-')
        #print (ips)

        if len(ips) == 1:
            # if one IP
            first_ip = ipaddress.ip_address(ips[0])
            ip.append(str(first_ip))

        else:
            ips1 = ips[0].split('.')
            ips2 = ips[1].split('.')
            if len(ips1) == 4 and len(ips2) == 4:
                #if 2 full IPs
                ip1 = ipaddress.ip_address(ips[0])
                ip2 = ipaddress.ip_address(ips[1])
                ip.append(str(ip1))

                while True:
                    ip1 = ip1 + 1
                    ip.append(str(ip1))
                    if ip1 >= ip2:
                        break

            else:
            #if range IPs
                ip1 = ipaddress.ip_address(ips[0])
                ip.append(str(ip1))
                ip2 = ipaddress.ip_address('.'.join(ips1[:3] + ips2))

                while True:
                    ip1 = ip1 + 1
                    ip.append(str(ip1))
                    if ip1 >= ip2:
                        break

    reachable = []
    unreachable = []

    for i in ip:
        print (i)


        reply = subprocess.run(['ping', '-c', '1', '-n', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

        if reply.returncode == 0:
                reachable.append(i)
        elif reply.returncode != 0:
                unreachable.append(i)

    d = {'Reachable' : [], 'Unreachable' : []}
    d['Reachable'] = reachable
    d['Unreachable'] = unreachable

    print (tabulate(d, headers='keys'))


list_ip = ['10.1.1.1-2']
check_ip_availability(list_ip)