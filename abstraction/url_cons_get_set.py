# TASK
# Реализуйте абстракцию для работы с URL. Она должна извлекать и менять части адреса.
#
# Интерфейс:
#
# make(url) - Конструктор. Создает URL.
# get_scheme(data) - Селектор (геттер). Извлекает схему.
# set_scheme(data, scheme) - Сеттер. Меняет схему.
# get_host(data) - Геттер. Извлекает host.
# set_host(data, host) - Сеттер. Меняет host.
# get_path(data) - Геттер. Извлекает путь.
# set_path(data, path) - Сеттер. Меняет путь.
# get_query_param(data, param_name, default=None) - Геттер. Извлекает значение для параметра запроса.
#                                                   Третьим параметром функция принимает значение по умолчанию,
#                                                   которое возвращается тогда, когда в запросе не было такого параметра
# set_query_param(data, key, value) - Сеттер. Устанавливает значение для параметра запроса.
#                                     Если передано значение None, то параметр отбрасывается.
# to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL, а старый оставлять неизменным.
#
#
# USAGE
# u = url.make('https://hexlet.io/community?q=low')
#
# u = url.set_scheme(u, 'http')
# url.to_string(u)  # 'http://hexlet.io/community?q=low'
# 
# u = url.set_path(u, '/404')
# url.to_string(u)  # 'http://hexlet.io/404?q=low'
# 
# url.get_query_param(u, 'q')  # 'low'
# 
# u = url.set_query_param(u, 'page', 5)
# url.to_string(u)  # 'http://hexlet.io/404?q=low&page=5'
# 
# u = url.set_query_param(u, 'q', 'high')
# url.to_string(u)  # 'http://hexlet.io/404?q=high&page=5'
# 
# u = url.set_query_param(u, 'q', None)
# url.to_string(u)  # 'http://hexlet.io/404?page=5'


from urllib.parse import urlparse, urlunparse, urlencode


def make(url_path):
    return url_path


def to_string(data):
    parce = urlparse(data)
    return str(urlunparse(parce))


def get_scheme(data):
    parce = urlparse(data)
    return parce.scheme


def get_host(data):
    parce = urlparse(data)
    return parce.hostname


def get_path(data):
    parce = urlparse(data)
    return parce.path


def get_query_param(data, name, default=None):
    res_dct = make_dict(data)
    if name in res_dct.keys() and default is None:
        return res_dct[name]
    elif default is not None:
        return default
    elif name not in res_dct.keys() and default is None:
        return None


def set_scheme(data, scheme):
    new_data = urlparse(data)._replace(scheme=scheme)
    return urlunparse(new_data)


def set_host(data, host):
    new_data = urlparse(data)._replace(netloc=host)
    return urlunparse(new_data)


def set_path(data, path):
    new_data = urlparse(data)._replace(path=path)
    return urlunparse(new_data)


def set_query_param(data, key, value):
    res_dct = make_dict(data)
    if value is not None:
        res_dct[key] = value
    elif key in res_dct.keys():
        del res_dct[key]
    new_query = urlencode(res_dct)
    new_data = urlparse(data)._replace(query=new_query)
    return urlunparse(new_data)


def make_dict(data):
    query_list = urlparse(data).query.split("&")
    res_dct = {}
    for _ in query_list:
        res_dct[_.split("=")[0]] = _.split("=")[1]
    return res_dct
