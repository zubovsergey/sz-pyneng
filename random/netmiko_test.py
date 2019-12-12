import getpass
import sys
from netmiko import ConnectHandler
from pprint import pprint

"""
def continue_break():

    ui = input('Continue? [Y/N] ')

    if ui.lower() in ('y', 'yes'):
        return True
    if ui.lower() in ('n', 'no'):
        break
"""

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

#user = input('Username: ')
#password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1']

for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'
    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()

        good = {}
        bad = {}


        for comm in commands:

            result = ssh.send_config_set(comm)

            if 'Incomplete command' in result:
                print ('Команда \"{}\" выполнилась с ошибкой "Incomplete command." на устройстве {}'.format(comm, ip))
                bad[comm] = result
                ui = input('Continue? [Y/N] ')
                if ui.lower() in ('y', 'yes'):
                    continue
                elif ui.lower() in ('n', 'no'):
                    break                    

            elif 'Invalid input' in result:
                print ('Команда \"{}\" выполнилась с ошибкой "Invalid input detected at \'^\' marker." на устройстве {}'.format(comm, ip))
                bad[comm] = result
                ui = input('Continue? [Y/N] ')
                if ui.lower() in ('y', 'yes'):
                    continue
                elif ui.lower() in ('n', 'no'):
                    break

            else:
                good[comm] = result

        result2 = good, bad    

        pprint(good.keys())
