# -*- coding: utf-8 -*-

import subprocess
import re
import socket
from pprint import pprint

def ping_ip_addresses (ip_list):

    alive_ips = {}
    unreachable_ips = []

    for ip in ip_list:
        data = socket.gethostbyname(ip)

        #alive_ips.append(repr(data))
        alive_ips[ip] = repr(data)

    
    return pprint (('Good IPs: ', alive_ips))
    #return alive_ips, unreachable_ips



if __name__ == '__main__':

	dns_list = []

	with open('qapresence_list.txt', 'r') as f:
		


		for line in f:
			match = re.search('(http[s]?:\/\/)', line).group()
			dns_list.append(line.strip('\n').strip('/').replace(match, ''))

	#print (dns_list)

	ping_ip_addresses(dns_list)
