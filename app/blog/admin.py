from django.contrib import admin
from app.blog import models
from app.blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

admin.site.register(KategoriModel)


@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik')
    list_display = ('baslik','olusturulma_tarihi','duzenlenme_tarihi')


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    search_fields = ('yazar__username',)
    list_display = ('yazar','olusturulma_tarihi','duzenlenme_tarihi')


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ('email','mesaj')
    list_display = ('email','olusturulma_tarihi')
