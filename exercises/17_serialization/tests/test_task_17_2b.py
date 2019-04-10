import os
import yaml
import pytest
import task_17_2b
import sys
sys.path.append('..')

from common_functions import check_function_exists, unify_topology_dict


def test_function_created():
    check_function_exists(task_17_2b, 'transform_topology')


def test_function_return_value(sh_cdp_topology_tuples):
    correct_return_value = unify_topology_dict(sh_cdp_topology_tuples)

    assert os.path.exists("topology.yaml"), "Файл topology.yaml не существует"
    return_value = task_17_2b.transform_topology("topology.yaml")
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == dict, "Функция должна возвращать словарь"
    assert unify_topology_dict(return_value) == correct_return_value, "Функция возвращает неправильное значение"

