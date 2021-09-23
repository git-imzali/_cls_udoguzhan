from django.shortcuts import render, get_object_or_404
from app.blog.models import YazilarModel, YorumModel


def detay(request, slug):

    yazi = get_object_or_404(YazilarModel, slug=slug)
    yorumlar = yazi.yazininyorumlari.all()

    context = {
        'yazi':yazi,
        'yorumlar':yorumlar,
    }

    return render(request, 'pages/detay.html', context)
