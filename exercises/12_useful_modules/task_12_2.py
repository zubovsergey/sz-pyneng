# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''

import subprocess
import ipaddress

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

    print ('Reachable IPs: ', reachable)
    print ('Unreachable IPs: ', unreachable)

list_ip = ['10.1.1.1-2']
check_ip_availability(list_ip)
