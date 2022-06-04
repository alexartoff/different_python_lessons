# Реализуйте функцию downcase_file_names, которая принимает на вход директорию (объект-дерево),
# приводит имена всех файлов в этой и во всех вложенных директориях к нижнему регистру.
# Результат в виде обработанной директории возвращается наружу.


import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def downcase_file_names(tree):
    name = get_name(tree)
    n_meta = copy.deepcopy(get_meta(tree))
    if is_file(tree):
        return mkfile(name.lower(), n_meta)
    chld = get_children(tree)
    n_chld = list(map(lambda ch: downcase_file_names(ch), chld))
    return mkdir(name, n_chld, n_meta)
