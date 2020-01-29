import netmiko
from pprint import pprint
import yaml
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat
from datetime import datetime
import time

logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

start_msg = '===> {} Connection to device: {}'
recieved_msg = '===> {} Recieved result from device: {}'

def send_show(device, show):
    ip = device['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            logging.info(recieved_msg.format(datetime.now().time(), ip))
            result = ssh.send_command(show)
            return {ip: result}
    except netmiko.NetMikoAuthenticationException as err:
        logging.warning(err)
            
if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.load(f, Loader=yaml.FullLoader)

with ThreadPoolExecutor(max_workers = 2) as executor:
    result = executor.map(send_show,devices,repeat('sh clock'))
    for output in result:
        print (output)
