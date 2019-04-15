# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['interface', 'duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as f:

    for line in f:

        skip_line = False

        for x in ignore:
            if x in line:
                #skip_line = True
                break          
            if not line.startswith('!') and not skip_line:
                print(line)            