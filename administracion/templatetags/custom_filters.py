from django import template


register = template.Library()

@register.filter
def miles(value):
    value = str(value)
    entero, decimal = value.split(".")
    lista = []
    for index in range(-1, -(len(entero)+1), -1):
        lista.append(entero[index])
        if index % 3 == 0 and index > -len(entero):
            lista.append(".")
    lista = lista[::-1]
    return "".join(lista) + "," + decimal

@register.filter
def create_range(value):
    return range(value)