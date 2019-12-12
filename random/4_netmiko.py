import getpass
import sys
from netmiko import ConnectHandler


command = sys.argv[1]
user = input('Username: ')
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']

for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': password,
        'secret': enable_pass
    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()

        result = ssh.send_command(command)
        print(result)