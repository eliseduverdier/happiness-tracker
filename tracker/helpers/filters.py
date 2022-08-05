from django.template.defaulttags import register

@register.filter
def get_attr(dictionary, key):
    return dictionary.get(key)
