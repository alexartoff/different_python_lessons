# Реализуйте функцию get_hidden_files_count, которая считает количество скрытых файлов в директории и
# всех поддиректориях. Скрытым файлом в Linux системах считается файл, название которого начинается с точки.


from hexlet.fs import get_children, get_name, is_file


def get_hidden_files_count(tree):
    name = get_name(tree)
    if is_file(tree) and get_name(tree)[0] == ".":
        return 1
    chld = get_children(tree)
    hidden_count = list(map(get_hidden_files_count, chld))
    return sum(hidden_count)


# Реализуйте функцию du, которая принимает на вход директорию, а возвращает список узлов,
# вложенных (директорий и файлов) в указанную директорию на один уровень, и место, которое они занимают.
# Размер файла задается в метаданных. Размер директории складывается из сумм всех размеров файлов,
# находящихся внутри во всех подпапках. Сами папки размера не имеют.
# !!!
# Обратите внимание на структуру результирующего cписка. Каждый элемент — кортеж с двумя значениями:
# именем директории и размером файлов внутри.
# Результат отсортирован по размеру в обратном порядке. То есть сверху самые тяжёлые, внизу самые лёгкие.


from hexlet.fs import get_children, get_meta, get_name, is_file, is_directory


def du(tree):
    chld = get_children(tree)
    filtered_dir = filter(is_directory, chld)
    result_dir = map(
        lambda child: (get_name(child), get_size(child)),
        filtered_dir,
    )
    filtered_file = filter(is_file, chld)
    result_file = map(
        lambda child: (get_name(child), get_size(child)),
        filtered_file,
    )
    res = sorted((list(result_dir) + list(result_file)),
                 key=lambda item: item[1],
                 reverse=True)
    return res


def get_size(node):
    if is_file(node):
        size = get_meta(node)["size"]
        return size
    chld = get_children(node)
    node_size = list(map(get_size, chld))
    return sum(node_size)
