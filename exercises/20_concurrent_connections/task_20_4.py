# -*- coding: utf-8 -*-
'''
Задание 20.4

Создать функцию send_commands_to_devices, которая отправляет команду show или config на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* show - команда show, которую нужно отправить (по умолчанию, значение None)
* config - команды конфигурационного режима, которые нужно отправить (по умолчанию, значение None)
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Пример вызова функции:
In [5]: send_commands_to_devices(devices, show='sh clock', filename='result.txt')

In [6]: cat result.txt
R1#sh clock
*04:56:34.668 UTC Sat Mar 23 2019
R2#sh clock
*04:56:34.687 UTC Sat Mar 23 2019
R3#sh clock
*04:56:40.354 UTC Sat Mar 23 2019

In [11]: send_commands_to_devices(devices, config='logging 10.5.5.5', filename='result.txt')

In [12]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.5.5.5
R1(config)#end
R1#config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#logging 10.5.5.5
R2(config)#end
R2#config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#logging 10.5.5.5
R3(config)#end
R3#

In [13]: send_commands_to_devices(devices,
                                  config=['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0'],
                                  filename='result.txt')

In [14]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router ospf 55
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#router ospf 55
R2(config-router)#network 0.0.0.0 255.255.255.255 area 0
R2(config-router)#end
R2#config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#router ospf 55
R3(config-router)#network 0.0.0.0 255.255.255.255 area 0
R3(config-router)#end
R3#


Для выполнения задания можно создавать любые дополнительные функции.
'''
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

from netmiko import ConnectHandler
import netmiko.ssh_exception
import yaml

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

start_msg = '===> {} Connection: {}'
received_msg = '<=== {} Received:   {}'

def send_show(device, command, verbose = True):
    if verbose:
        print('connection to device {}'.format(device['ip']))
    device_params = device
    try:
        logging.info(start_msg.format(datetime.now().time(), device['ip']))
        ssh = ConnectHandler(**device_params)
        ssh.enable()
        result = ssh.find_prompt()  + command + '\n' + ssh.send_command(command) + '\n'*2
        logging.info(received_msg.format(datetime.now().time(), device['ip']))

    except netmiko.ssh_exception.SSHException as err:
        print (err)

    return result

def send_config(device, command, verbose = True):
    if verbose:
    	print('connection to device {}'.format(device['ip']))
    device_params = device  
    try:
        logging.info(start_msg.format(datetime.now().time(), device['ip']))
        ssh = ConnectHandler(**device_params)
        ssh.enable()
        result = ssh.send_config_set(command) + '\n'*2
        logging.info(received_msg.format(datetime.now().time(), device['ip']))
    except netmiko.ssh_exception.SSHException as err:
        print (err)

    return result


def send_commands_to_devices(devices, filename, limit, show = None, config = None):
    data = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = []
        for device in devices:
            if show:
                futures.append(executor.submit(send_show, device, show))
            elif config:
                futures.append(executor.submit(send_config, device, config))

        for f in as_completed(futures):
            data.append(f.result())

    with open(filename, 'w') as dest:
        for line in data:
            dest.write(line)

if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        send_commands_to_devices(devices, 'result.txt', 3,config=['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0'])

        #for device in devices:
        	#print (send_show(device,'sh clock'))

