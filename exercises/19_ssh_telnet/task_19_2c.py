# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''
import getpass
import sys
import netmiko.ssh_exception
from netmiko import ConnectHandler
import yaml
from pprint import pprint

# списки команд с ошибками и без:

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

def send_config_command(device, comm, verbose = True):

  good = {}
  bad = {}

  if verbose:
    print('connection to device {}'.format(device['ip']))
  device_params = device

  try:
    ssh = ConnectHandler(**device_params)
    ssh.enable()

    for comm in commands:

      result = ssh.send_config_set(comm)

      if 'Incomplete command' in result:
            print ('Команда \"{}\" выполнилась с ошибкой "Incomplete command." на устройстве {}'.format(comm, device['ip']))
            bad[comm] = result
            ui = input('Continue? [Y/N] ')
            if ui.lower() in ('y', 'yes'):
                  continue
            elif ui.lower() in ('n', 'no'):
                  break  
      elif 'Invalid input' in result:
            print ('Команда \"{}\" выполнилась с ошибкой "Invalid input detected at \'^\' marker." на устройстве {}'.format(comm, device['ip']))
            bad[comm] = result
            ui = input('Continue? [Y/N] ')
            if ui.lower() in ('y', 'yes'):
                  continue
            elif ui.lower() in ('n', 'no'):
                  break  
      else:
            good[comm] = result

  except netmiko.ssh_exception.SSHException as err:
    print (err)

  result2 = good, bad  

  pprint(result2, width=120)

if __name__ == '__main__':

  with open ('devices.yaml') as f:
      device_list = yaml.safe_load(f)

      for device in device_list:
        
        send_config_command(device, commands)

