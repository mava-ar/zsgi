from django.template.defaulttags import register

from zweb_utils.format import currency_format


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def money(val):
    return currency_format(val)

