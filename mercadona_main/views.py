from django.shortcuts import render
from category.models import Category
from store.models import Product, ReviewRating
import django

def home(request):
    categories = Category.objects.all()[:3]
    products = Product.objects.all().filter(is_available=True).order_by('created_date')[:8]
    print(django.get_version())
    
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'categories': categories,
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)