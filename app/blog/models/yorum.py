from django.db import models
from django.contrib.auth.models import User
from app.blog.models import YazilarModel

class YorumModel(models.Model):
    
    yorum = models.TextField()

    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)
    
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazarinyorumlari')
    yazi  = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yazininyorumlari')

    class Meta:
        db_table = 'yorum'
        verbose_name='Yorum'
        verbose_name_plural='Yorumlar'

    def __str__(self):
        return self.yorum[:40]
        #return self.yazar.username