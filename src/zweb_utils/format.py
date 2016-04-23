import locale


def decimal_format(val):
    """
    Dado un valor numérico, retorna un string en formato número con dos decimales y separados de miles
    :param val: número
    :return: string formateado
    """
    locale.setlocale(locale.LC_ALL, '')
    return "{}".format(locale.format('%.2f', val, 1))


def currency_format(val):
    """
    Dado un valor numérico, retorna un string en formato "dinero"
    :param val: número
    :return: string formateado
    """
    return "$ {}".format(decimal_format(val))


def number_js_format(val):
    """

    :param val:
    :return:
    """
    num = "{:.2f}".format(val)

    return num
