from django.template.defaulttags import register

from zweb_utils.format import currency_format, decimal_format, number_js_format


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def money(val):
    return currency_format(val)


@register.filter
def js_format(val):
    return number_js_format(val)