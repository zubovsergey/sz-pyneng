# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

commands1 = command1.strip().split()
vlans1 = commands1[-1].strip().split(',')
commands2 = command2.strip().split()
vlans2 = commands2[-1].strip().split(',')

common_vlans = set(vlans1) & (set(vlans2))
print (list(common_vlans))