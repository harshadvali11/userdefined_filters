from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

@register.filter()
def counting(value,arg):
    return value.count(arg)

@register.filter(name='rem')
def remove(value,arg):
    return value.replace(arg,'')

register.filter('swapping',swap)
#register.filter('counting',counting)
#register.filter('remove',remove)




