# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import logging
from datetime import datetime
import time

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

start_msg = '===> {} pinging ip: {}'
recieved_msg = '===> {} Recieved result from ip: {}'

def ping_ip_address(ip):
    if ip:
        p = subprocess.Popen(['ping', '-c', '3', '-n', ip],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        returncode = p.wait()
    return ip, returncode      

def ping_ip_addresses(ip_list, limit):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip_address, ip_list)
        for output in result:
            if output[1] == 0:
                reachable.append(output[0])
            else:
                unreachable.append(output[0])
    return reachable, unreachable

    """"
    OR:
    with ThreadPoolExecutor(max_workers=limit) as executor:
    futures = []
    for ip in ip_list:
        result = executor.submit(ping_ip_address, ip)
        futures.append(result)
    for f in as_completed(futures):
        if f.result()[1] == 0:
            reachable.append(f.result()[0])
        else:
            unreachable.append(f.result()[0])
    """

if __name__ == "__main__":

	ip_list = ['8.8.8.8', '192.168.100.22', '192.168.100.1']
	print(ping_ip_addresses(ip_list, 3))