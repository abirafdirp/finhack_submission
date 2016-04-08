import json

from django import template


register = template.Library()


@register.filter
def locationsjson(objects):
    objectss = objects.values_list('name', 'longitude', 'latitude')
    return json.dumps(obj=list(objectss))


@register.filter
def countersjson(objects):
    print(objects)
    objectss = objects.values_list('name', 'address', 'city', 'latitude', 'longitude')
    return json.dumps(obj=list(objectss))
