from django.contrib import admin
from app.blog import models
from app.blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik')
    list_display = ('baslik','olusturulma_tarihi','duzenlenme_tarihi')

admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    search_fields = ('yazar__username',)
    list_display = ('yazar','olusturulma_tarihi','guncellenme_tarihi')

admin.site.register(YorumModel, YorumAdmin)

class IletisimAdmin(admin.ModelAdmin):
    search_fields = ('email','mesaj')
    list_display = ('email','olusturulma_tarihi')

admin.site.register(IletisimModel, IletisimAdmin)