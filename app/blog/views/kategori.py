from django.shortcuts import render, get_object_or_404
from app.blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator

def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)

    yazilar = kategori.kategoriyazilari.order_by('-id')

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 1)
    data = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request, 'pages/anasayfa.html', context=data)