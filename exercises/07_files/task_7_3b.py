# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('CAM_table.txt') as f:
    result = []
    for line in f:
        line = line.strip().split()
        if line and line[0].isdigit():
            vlan, mac, _ , interface = line
            x = vlan, mac, interface
            y = list(x)
            result.append(y)

    vlan = input('Enter vlan number: ')
    result.sort()
    for z in result:
        if int(vlan) == int(z[0]):
            print (' '.join(z))