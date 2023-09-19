from django.shortcuts import render


def get_start_page(request):
    return render(request, 'index.html')
