from django.shortcuts import render
from .models import New


def news(request):
    news = New.objects.all()
    return render(request, 'news.html', context={'news': news})


def detail(request, pk):
    new = New.objects.get(pk__iexact=pk)
    return render(request, 'detail.html', context={'new': new})
