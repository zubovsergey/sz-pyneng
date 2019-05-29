# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map (filename):

    with open(filename) as f:
        result_access = {}
        result_trunk = {}
        for line in f:
            if 'interface FastEthernet' in line:
                intf = line.split()[-1]
                result_access[intf] = '1'
            elif 'switchport access vlan' in line:
                result_access[intf] = line.split()[-1]
            elif 'switchport trunk allowed vlan' in line:
                result_trunk[intf] = line.split()[-1]
                del(result_access[intf])
        return result_access, result_trunk

print(get_int_vlan_map('config_sw2.txt'))