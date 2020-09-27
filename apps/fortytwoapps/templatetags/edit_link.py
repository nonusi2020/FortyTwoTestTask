from django.urls import reverse
from django import template


register = template.Library()


@register.simple_tag
def edit_link(obj, *args):
    """
    A template tag which accepts any object and renders a link to its admin edit page
    """
    try:
        arguments = args
        if args:
            view_name = 'admin:{}_change'.format(obj._meta.db_table)
        else:
            view_name = 'admin:{}_changelist'.format(obj._meta.db_table)

        return reverse(view_name, args=arguments)
    except AttributeError:
        raise template.TemplateSyntaxError("{} isn't correct object".format(obj))
