from django.utils.translation import to_locale, get_language
from django import template
import locale
register = template.Library()


#Need Implement Intenationalization

@register.filter
def as_currency(value):
    print(to_locale(get_language()))
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    formated_value = locale.currency(value, grouping=True)
    return formated_value