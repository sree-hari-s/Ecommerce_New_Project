from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {'products':products}
    return render(request,'home.html',context)

def handle_not_found(request,exception):
    return render(request,'customerror/404.html')