# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input ('Enter ip address: ')
#ip = '10.1.1.1'

while True:

    if len(ip.split('.')) == 4 and 0 <=int(ip.split('.')[0]) <= 255 and 0 <=int(ip.split('.')[1]) <= 255 and 0 <=int(ip.split('.')[2]) <= 255 and 0 <=int(ip.split('.')[3]) <= 255:

        if  1 <= int(ip.split('.')[0]) <= 223:
            print (ip + ' - unicast')
        elif 2 <= int(ip.split('.')[0]) <= 239:
            print (ip + ' - multicast')
        elif ip == '255.255.255.255':
            print (ip + ' - local broadcast')
        elif ip == '0.0.0.0':
            print (ip + ' - unassigned')
        else:
            print (ip + 'unused')
        break
    ip = input ('Enter ip address again: ')
