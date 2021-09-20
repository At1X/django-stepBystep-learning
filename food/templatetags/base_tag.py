from django import template
from django.utils import timezone
from ..models import Category

register = template.Library()
@register.simple_tag()
def showTime():
    return timezone.now()


@register.inclusion_tag('categ_tags.html')
def profCateg():
    return {
        'cat': Category.objects.all()
    }