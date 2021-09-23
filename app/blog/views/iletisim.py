from django.shortcuts import render, redirect
from app.blog.forms import IletisimForm
from app.blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm(initial={
        'email':'no-name@gmail.com',
    })
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            #form.cleaned_data.get('email')
            #ilt = IletisimModel()
            #ilt.email = form.cleaned_data.get('email')
            #ilt.isim_soyisim = form.cleaned_data['isim_soyisim']
            #ilt.mesaj = form.cleaned_data['mesaj']
            #ilt.save()
            form.save()
            return redirect('anasayfa')

    data = {
        'form':form,
    }
    return render(request, 'pages/iletisim.html', context=data)