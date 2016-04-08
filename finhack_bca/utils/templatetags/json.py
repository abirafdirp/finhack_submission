import json

from django import template


register = template.Library()

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@register.filter
def locationsjson(objects):
    objectss = objects.values()
    return json.dumps(obj=list(objectss), default=date_handler)


@register.filter
def countersjson(objects):
    objectss = objects.values()
    return json.dumps(obj=list(objectss), default=date_handler)
