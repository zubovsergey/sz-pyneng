#!/usr/bin/env python3

with open('config.txt') as f:
    for line in f:
        line = line.rstrip().split()
        #print (line)


        if line:
            fex = line[3].split('-')[2]
            #print (fex)
            port = line[-1]
            #print (port)
            #print ('show int status | i {}'.format(fex.replace('FEX', 'Eth') +'/1/' + port.replace('p','')))
            print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))

        
        if line:
            description = line[0:2]
            #print (description)
            print ('description ' + ' '.join(description) + '\n switchport access vlan 133' + '\n   spanning-tree port type edge' '\n no shutdown')
