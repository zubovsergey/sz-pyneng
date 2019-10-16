
"""
     
            if line:
                description = line
                x = description.strip('').split('-')
                print (x)
                print ('description ' + ' '.join(description) + '\n switchport access vlan 506' + '\n no shutdown')



              
                if 'MBX027' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 139' + '\n no shutdown')

                if 'MBX028' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 101' + '\n no shutdown')

                if 'MBX128' in ' '.join(description):
                    print ('description ' + ' '.join(description) + '\n switchport access vlan 270' + '\n no shutdown')
"""
"""
        if '5648' in line:
            line = line.rstrip().split()
            fex = line[0].split('-')[-1]
            port = line[1]
            print ('interface ' + fex.replace('FEX', 'Ethernet') +'/1/' + port.replace('p',''))
        else:
            print ('description ' + line + 'switchport access vlan 139' + '\n no shutdown')
"""
"""