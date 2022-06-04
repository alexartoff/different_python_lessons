# TASK
# Реализуйте функцию find_files_by_name(), которая принимает на вход файловое дерево и подстроку,
# а возвращает список файлов, имена которых содержат эту подстроку. Функция должна вернуть полные пути файлам.
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
# HINTS
# 1.Для реализации этой логики вам понадобится аккумулятор, в котором будет храниться путь от корня до текущего узла.
#   При проваливании внутрь директорий к нему добавляется имя текущей директории. В остальном логика работы идентична примеру из теории.
# 2.Переменную, содержащую внутри себя путь от корня до текущего узла, можно назвать ancestry.
# 3.Для построения путей используйте функцию os.path.join().


import os

from hexlet.fs import flatten, get_children, get_name, is_file


def find_files_by_name(tree, file_name):
    def walk(node, ancestry):
        name = get_name(node)
        chld = get_children(node)
        if is_file(node) and file_name in name:
            file_path = os.path.join(ancestry, name)
            return file_path
        output = map(lambda ch: walk(ch, os.path.join(ancestry, name)), chld)
        return flatten(output)
    return walk(tree, '')
