from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def get_start_page(request):
    return render(request, 'base.html')


def booktable(request):
    return render(request, 'booktable.html')
