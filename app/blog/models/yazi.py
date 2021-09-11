from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from app.blog.models import KategoriModel
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    baslik = models.CharField(max_length=100,blank=False,null=False)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik',unique=True)
    resim =models.ImageField(upload_to='yazi_resimleri')
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='kategoriyazilari')
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazarinyazilari')

    class Meta:
        db_table = 'yazi'
        verbose_name='Yazı'
        verbose_name_plural='Yazılar'

    def __str__(self):
        return self.baslik
