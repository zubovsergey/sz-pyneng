# -*- coding: utf-8 -*-

import subprocess
import re
import socket

def ping_ip_addresses (ip_list):

    alive_ips = []
    unreachable_ips = []

    for ip in ip_list:
        reply = subprocess.run(['ping', '-c', '2', '-n', ip], stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            alive_ips.append(ip)
        else:
            unreachable_ips.append(ip)
    
    return print ('Good IPs: ', alive_ips), print ('Bad IPs: ', unreachable_ips)
    #return alive_ips, unreachable_ips



if __name__ == '__main__':

	dns_list = []

	with open('qapresence_list.txt', 'r') as f:
		


		for line in f:
			match = re.search('(http[s]?:\/\/)', line).group()
			dns_list.append(line.strip('\n').strip('/').replace(match, ''))

	print (dns_list)

	print (ping_ip_addresses(dns_list))