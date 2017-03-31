from django import template
register = template.Library()

@register.filter(name='Split')
def Split(string, index):
    return string.split(",")[index]

@register.filter(name='split')
def split(string, token):
    return string.split(token)

@register.filter(name='Round')
def Round(string, token):
    return round(float(string), token)

@register.filter(name='Slice')
def Slice(string, index):
    return string[0:int(index)]
