# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import getpass
import sys
from netmiko import ConnectHandler
import yaml
from pprint import pprint

command = 'sh ip int br'

def send_show_command (device):

	print('connection to device {}'.format(device['ip']))
	device_params = device

	with ConnectHandler(**device_params) as ssh:
		ssh.enable()

		result = ssh.send_command(command)

		pprint(result)




if __name__ == '__main__':

	with open ('devices.yaml') as f:
			device_list = yaml.safe_load(f)

			for device in device_list:
				
				send_show_command(device)

