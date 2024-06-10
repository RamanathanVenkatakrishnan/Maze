"""from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Category
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    product_data = [{'id': product.id, 'description': product.description, 'unit_price': product.unit_price} for product in products]
    return JsonResponse(product_data, safe=False)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_data = {
        'id': product.id,
        'description': product.description,
        'unit_price': product.unit_price,
        'categories': [category.name for category in product.categories.all()],
        'details':  product.CharField(max_length=255, null=True, blank=True),
        'stockquantity':  product.IntegerField(default=0)
    }
    return JsonResponse(product_data)

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'id': product.id,
                'description': product.description,
                'unit_price': product.unit_price,
                'categories': [category.name for category in product.categories.all()]
            }, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return HttpResponse('Method not allowed', status=405)

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'id': product.id,
                'description': product.description,
                'unit_price': product.unit_price,
                'categories': [category.name for category in product.categories.all()]
            }, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return HttpResponse('Method not allowed', status=405)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse('Method not allowed', status=405) """
        
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Category
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    product_data = [{'id': product.id, 'description': product.description, 'unit_price': product.unit_price} for product in products]
    return JsonResponse(product_data, safe=False)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_data = {
        'id': product.id,
        'description': product.description,
        'unit_price': product.unit_price,
        'categories': [category.name for category in product.categories.all()],
        'details': product.details,
        'stockquantity': product.stockquantity
    }
    return JsonResponse(product_data)

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'id': product.id,
                'description': product.description,
                'unit_price': product.unit_price,
                'categories': [category.name for category in product.categories.all()],
                'details': product.details,
                'stockquantity': product.stockquantity
            }, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return HttpResponse('Method not allowed', status=405)

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                'id': product.id,
                'description': product.description,
                'unit_price': product.unit_price,
                'categories': [category.name for category in product.categories.all()],
                'details': product.details,
                'stockquantity': product.stockquantity
            }, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return HttpResponse('Method not allowed', status=405)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse('Method not allowed', status=405)
 
 
        
