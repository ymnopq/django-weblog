from django.shortcuts import render, redirect


def home_page(request):
    context = {
        'data': 'new data'
    }
    return render(request, 'home_page.html', context)


def header(request):
    return render(request, 'shared/Header.html')


def footer(request):
    return render(request, 'shared/Footer.html')
