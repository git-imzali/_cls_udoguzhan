from django.shortcuts import render

def iletisim(request):
    data = {
        'ulke':'Türkiye'
    }
    return render(request, 'pages/iletisim.html', context=data)