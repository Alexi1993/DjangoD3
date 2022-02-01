from django import template

register = template.Library()


@register.filter(name='Censor')
def Censorship(value):
    censor_list = ['дурак',
                   'придурок']
    value1 = (str(value)).split()
    for i in censor_list:
        for j in value1:
            if j == i:
                value1.remove(i)
    value = ' '.join(value1)
    return str(value)
