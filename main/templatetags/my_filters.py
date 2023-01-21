from django import template

register = template.Library()

@register.filter
def longitude(cycle):
    return cycle.current_location.split(',')[1]

@register.filter
def latitude(cycle):
    return cycle.current_location.split(',')[0]
    