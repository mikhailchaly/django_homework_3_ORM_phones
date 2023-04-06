from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    get_page = request.GET.get('sort', '')
    template = 'catalog.html'
    phones = Phone.objects.all()

    if get_page == 'min_price':
        phones = Phone.objects.all().order_by('price')

    if get_page == 'max_price':
        phones = Phone.objects.all().order_by('-price')

    if get_page == 'name':
        phones = Phone.objects.all().order_by('name')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
