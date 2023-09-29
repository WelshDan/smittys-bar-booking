from django.shortcuts import render, get_object_or_404


def get_base(request):
    return render(request, 'base.html')


def get_booktable(request):
    return render(request, 'booktable.html')


def get_index(request):
    return render(request, 'index.html')
