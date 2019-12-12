# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''

import getpass
import sys
import netmiko.ssh_exception
from netmiko import ConnectHandler
import yaml
from pprint import pprint

command = 'sh ip int br'

def send_show_command (device):

	print('connection to device {}'.format(device['ip']))
	device_params = device

	try:
		ssh = ConnectHandler(**device_params)
		ssh.enable()

		result = ssh.send_command(command)

		pprint(result)
	except netmiko.ssh_exception.SSHException as err:
		print (err)





if __name__ == '__main__':

	with open ('devices.yaml') as f:
			device_list = yaml.safe_load(f)

			for device in device_list:
				
				send_show_command(device)

