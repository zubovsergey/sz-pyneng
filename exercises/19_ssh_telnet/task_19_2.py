# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#logging 10.255.255.1\nR1(config)#logging buffered 20010\nR1(config)#no logging console\nR1(config)#end\nR1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#


Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''
import getpass
import sys
import netmiko.ssh_exception
from netmiko import ConnectHandler
import yaml
from pprint import pprint

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_config_command(device, comm):

	print('connection to device {}'.format(device['ip']))
	device_params = device

	try:
		ssh = ConnectHandler(**device_params)
		ssh.enable()

		result = ssh.send_config_set(comm)

		pprint(result)
	except netmiko.ssh_exception.SSHException as err:
		print (err)


if __name__ == '__main__':

	with open ('devices.yaml') as f:
			device_list = yaml.safe_load(f)

			for device in device_list:
				
				send_config_command(device, commands)

