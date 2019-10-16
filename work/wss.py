#!/usr/bin/env python3

with open('wss_table.txt') as f:
    for line in f:
    	x = line.strip().split(',')
    	wss_subnet = x[9]
    	wss_name = x[10]
    	sql = x[12]
    	exch = x[10][3:]

    	print ('object-group network exvsql-{}-e'.format(exch))
    	print ("network-object {} 255.255.255.255".format(sql))
    	print ('object-group network {}'.format(wss_name))
    	print ('network-object {} 255.255.255.224'.format(wss_subnet))
    	print ('access-list EDGE line 20 extended permit object-group exvsql-ports object-group {} object-group exvsql-{}-e'.format (wss_name, exch))