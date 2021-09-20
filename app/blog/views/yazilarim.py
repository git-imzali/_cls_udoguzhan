from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='anasayfa')
def yazilarim(request):

    yazilar = request.user.yazarinyazilari.order_by('-id')

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)
    data = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request, 'pages/yazilarim.html', context=data)