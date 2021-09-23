from django.urls import path
from app.blog import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>/', views.kategori, name='kategori'),
    path('yazilarim/', views.yazilarim, name='yazilarim'),
    path('detay/<slug:slug>/', views.detay, name='detay'),
]
