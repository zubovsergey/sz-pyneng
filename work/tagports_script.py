#!/usr/bin/env python3

with open('config.txt') as f:
    for line in f:
        line = line.rstrip().split()
        #print (line)

       
        if line:
            fex = line[4].split('-')[4]
            #print (fex)
            port = line[-1]
            #print (port)
            #print ('show int status | i {}'.format(fex.replace('FEX', 'Eth') +'/1/' + port.replace('p','')))
            print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))

       
            if line:
                description = line[0:4]
                #x = description.strip('').split('-')
                #print (x)
                #print ('description ' + ' '.join(description) + '\n switchport access vlan 506' + '\n no shutdown')
                
                if 'MBX027' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 139' + '\n no shutdown')

                if 'MBX028' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 140' + '\n no shutdown')

                if 'MBX128' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 140' + '\n no shutdown')

"""
        if '5648' in line:
            line = line.rstrip().split()
            fex = line[0].split('-')[-1]
            port = line[1]
            print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))
        else:
            print ('description ' + line + 'switchport access vlan 139' + '\n no shutdown')
"""