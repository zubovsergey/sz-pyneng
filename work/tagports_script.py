#!/usr/bin/env python3

with open('config.txt') as f, open('result.txt', 'w') as f2:
    for line in f:
        #line = line.rstrip().split()

        """
        #if line:
            #fex = line[3].split('-')[-1]
            #port = line[4]
            #print ('show int status | i {}'.format(fex.replace('FEX', 'Eth') +'/1/' + port.replace('p','')))
            #print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))
        
            if line:
                description = line[0]
                #print (description.strip('#').split('-'))
                if '025' in description:
                    #print ('description ' + description + '\n switchport access vlan 139' + '\n no shutdown')
                if '026' in description:
                    #print ('description ' + description + '\n switchport access vlan 140' + '\n no shutdown')
        """


        if '5648' in line:
            line = line.rstrip().split()
            fex = line[0].split('-')[-1]
            port = line[1]
            print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))
        else:
            print ('description ' + line + 'switchport access vlan 139' + '\n no shutdown')