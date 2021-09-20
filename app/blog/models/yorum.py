from django.db import models
#from django.contrib.auth.models import User
from apaccount.models import CustomUserModel
from app.blog.models import YazilarModel
from app.blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    
    yorum = models.TextField()
    
    yazar = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='yazarinyorumlari')
    yazi  = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yazininyorumlari')

    class Meta:
        db_table = 'yorum'
        verbose_name='Yorum'
        verbose_name_plural='Yorumlar'

    def __str__(self):
        return self.yorum[:40]
        #return self.yazar.username