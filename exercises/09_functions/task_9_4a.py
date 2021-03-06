# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4, но функция convert_config_to_dict должна поддерживать еще один уровень вложенности.
При этом, не привязываясь к конкретным разделам в тестовом файле.
Функция должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

При записи команд в словарь, пробелы в начале строки надо удалить.

Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Секция итогового словаря на примере interface Ethernet0/3.100:

'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}

Примеры других секций словаря можно посмотреть в тесте к этому заданию.
Тест проверяет не весь словарь, а несколько разнотипных секций.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from pprint import pprint
ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config):
    result = {}
    with open(config) as f:
        for line in f:
            line = line.rstrip()

            if line and not ('!' in line or ignore_command(line, ignore)):
                if line[0].isalnum():
                    level_1 = line
                    result[level_1] = []
                elif line.startswith(' ') and line[1].isalnum():
                    last_level_2 = line
                    result[level_1].append(line)
                else:
                    #если команда 3 уровня встретилась первый раз,
                    #результатом будет список
                    if type(result[level_1]) is list:
                        result[level_1] = {key:[] for key in result[level_1]}
                    result[level_1][last_level_2].append(line)

    return result
pprint(convert_config_to_dict('config_r1.txt'))
