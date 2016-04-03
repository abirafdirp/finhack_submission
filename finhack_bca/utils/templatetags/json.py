import json

from django import template


register = template.Library()


@register.filter
def dumpjson(objects):
    print(objects)
    objectss = objects.values_list('name', 'longitude', 'latitude')
    print(objectss)
    return json.dumps(obj=list(objectss))
