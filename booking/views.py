from django.shortcuts import render, get_object_or_404


def get_start_page(request):
    return render(request, 'base.html')
