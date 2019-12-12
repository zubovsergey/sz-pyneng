# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
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
		with ConnectHandler(**device_params) as ssh:
			ssh.enable()

			result = ssh.send_command(command)

			pprint(result)
	except netmiko.NetMikoAuthenticationException as err:
		print (err)




if __name__ == '__main__':

	with open ('devices.yaml') as f:
			device_list = yaml.safe_load(f)

			for device in device_list:
				
				send_show_command(device)

