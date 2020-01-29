import netmiko
from pprint import pprint
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    #if ip == '192.168.100.1': time.sleep(5)
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            logging.info(recieved_msg.format(datetime.now().time(), ip))
            result = ssh.send_command(show)
            return {ip: result}
    except NetMikoAuthenticationException as err:
        logging.warning(err)
            
if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.load(f, Loader=yaml.FullLoader)

with ThreadPoolExecutor(max_workers = 3) as executor:
    futures = []
    for device in devices:
        futures.append(executor.submit(send_show, device, 'sh clock'))
    print (futures)
    for f in as_completed(futures):
        print ('#'*54)
        print(f.result())
        print ('#'*54)