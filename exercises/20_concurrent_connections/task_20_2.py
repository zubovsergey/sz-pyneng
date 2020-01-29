# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import logging

from netmiko import ConnectHandler
import yaml

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

start_msg = '===> {} Connection: {}'
received_msg = '<=== {} Received:   {}'

def send_show(device_dict, command):
    logging.info(start_msg.format(datetime.now().time(), device_dict['ip']))
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.find_prompt()  + command + '\n' + ssh.send_command(command) + '\n'*2
        logging.info(received_msg.format(datetime.now().time(), device_dict['ip']))
        return result

def send_command_to_devices(devices, command, filename, limit):
    data = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for output in result:
            data.append(output)
    with open(filename, 'w') as dest:
        for line in data:
            dest.write(line)





if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    pprint(send_command_to_devices(devices, 'sh ip int br', 'result.txt', 3))
