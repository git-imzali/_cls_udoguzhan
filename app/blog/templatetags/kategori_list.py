from django import template
from django.contrib.admin.decorators import register
from app.blog.models import KategoriModel

register = template.Library()

@register.simple_tag
def kategori_list():
    kategoriler = KategoriModel.objects.all()
    return kategoriler