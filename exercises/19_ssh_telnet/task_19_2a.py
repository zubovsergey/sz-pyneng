# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
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

def send_config_command(device, comm, verbose = True):

	if verbose:
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
				
				send_config_command(device, commands, verbose = False)
 