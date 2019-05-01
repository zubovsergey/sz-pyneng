# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def ping_ip_addresses (ip_list):

    alive_ips = []
    unreachable_ips = []

    for ip in ip_list:
        reply = subprocess.run(['ping', '-c', '1', '-n', ip], stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            alive_ips.append(ip)
        else:
            unreachable_ips.append(ip)
    
    return print ('Good IPs: ', alive_ips), print ('Bad IPs: ', unreachable_ips)
    #return alive_ips, unreachable_ips



ip_list = ['8.8.8.8', '4.4.4.4']

print (ping_ip_addresses(ip_list))