from django.shortcuts import render, get_object_or_404


def get_basepage(request):
    return render(request, 'base.html')


def get_booktable(request):
    return render(request, 'booktable.html')


def get_indexpage(request):
    return render(request, 'index.html')
