# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv 
ip_addr = argv[1:] 

ip_template = '''
   NETWORK:
   {0:<8} {1:<8} {2:<8} {3:<8}
   {0:<08b} {1:<08b} {2:<08b} {3:<08b}
   '''

mask_template = '''
   MASK:
   {0:<8} {1:<8} {2:<8} {3:<8}
   {0:<08b} {1:<08b} {2:<08b} {3:<08b}
   '''

#ip_addr = input ("Enter ip network:")

#ip_addr = '10.2.0.0/23'

mask = ip_addr[0].strip().split('/')[-1]
ip = ip_addr[0].strip().split('/')[0]

mask_2 = '1'*int(mask) + '0'*(32-int(mask))

subnet1 = int(ip.split('.')[0]) & int(mask_2[0:8], 2)
subnet2 = int(ip.split('.')[1]) & int(mask_2[8:16], 2) 
subnet3 = int(ip.split('.')[2]) & int(mask_2[16:24], 2) 
subnet4 = int(ip.split('.')[3]) & int(mask_2[24:32], 2) 


print(ip_template.format(subnet1,subnet2,subnet3,subnet4))
print(ip_template.format(int(mask_2[0:8],2),int(mask_2[8:16],2),int(mask_2[16:24],2),int(mask_2[24:32],2)))