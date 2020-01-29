# -*- coding: utf-8 -*-
'''
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
'''
import re
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed

command = 'sh ip int br | i Tu'

data = {
    'tun_num': None,
    'wan_ip_1': '192.168.100.1',
    'wan_ip_2': '192.168.100.2',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
}

src_r = {'device_type': 'cisco_ios',
              'ip': '192.168.100.1',
              'username': 'cisco',
              'password': 'cisco',
              'secret': 'cisco'}

dst_r = {'device_type': 'cisco_ios',
              'ip': '192.168.100.2',
              'username': 'cisco',
              'password': 'cisco',
              'secret': 'cisco'}

def send_show_command (device):
	print('connection to device {}'.format(device['ip']))
	device_params = device
	with ConnectHandler(**device_params) as ssh:
		ssh.enable()
		result =ssh.send_command(command)
		return result

def check_tu_int (device1, device2):
	with ThreadPoolExecutor(max_workers=2) as executor:
		futures = []
		futures.append(executor.submit(send_show_command, device1))
		futures.append(executor.submit(send_show_command, device2))

		for f in as_completed(futures):
			if f.result():
				y = []
				x = f.result()
				match = re.findall('(Tunnel)(\d+)', x)
				for i in match:
					y.append(int(i[1]))
				int_num = []
				for i2 in range(1, 1000):
					if i2 not in y:
						int_num.append(i2)

				return int_num[0]

def configure_vpn (src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
	env = Environment(
		loader=FileSystemLoader('templates'),
		trim_blocks=True,
		lstrip_blocks=True)
	temp1 = env.get_template(src_template)
	temp2 = env.get_template(dst_template)
	
	config = vpn_data_dict
	config['tun_num'] = check_tu_int(src_device_params,dst_device_params)

	result1 = temp1.render(config)
	result2 = temp2.render(config)

	final = [result1, result2]

	return final

if __name__ == '__main__':
	pprint(configure_vpn (src_r, dst_r, 'gre_ipsec_vpn_1.txt','gre_ipsec_vpn_2.txt', data))