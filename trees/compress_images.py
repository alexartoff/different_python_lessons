# Реализуйте функцию compress_images(), которая принимает на вход директорию, находит внутри
# нее картинки и "сжимает" их. Под сжиманием понимается уменьшение свойства size в метаданных
# в два раза. Функция должна вернуть обновленную директорию со сжатыми картинками и всеми
# остальными данными, которые были внутри этой директории.
# Картинками считаются все файлы, заканчивающиеся на .jpg.


import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(tree):
    chld = get_children(tree)
    new_chld = list(map(half_image_size, chld))
    new_meta = copy.deepcopy(get_meta(tree))
    new_tree = mkdir(get_name(tree), new_chld, new_meta)
    return new_tree


def half_image_size(node):
    name = get_name(node)
    chld = get_children(node)
    n_chld = chld[:]
    n_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        if ".jpg" in name:
            n_meta['size'] = int(n_meta['size'] / 2)
        return mkfile(name, n_meta)
    return mkdir(name, n_chld, n_meta)
