from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.favorites.models import Favorite
from django.db.models import Avg
from .models import Product
from apps.reviews.models import Review

def index(request):
    products = Product.objects.all()

    favorite_ids = []

    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list("product_id", flat=True)

    return render(request, "index.html", {
        "products": products,
        "favorite_ids": favorite_ids
    })


def product_detail(request, pk):

    product = get_object_or_404(Product, id=pk)

    reviews = Review.objects.filter(product=product)

    avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]

    return render(request, "product.html", {
        "product": product,
        "reviews": reviews,
        "avg_rating": avg_rating
    })

def search(request):
    q = request.GET.get("q", "")

    products = Product.objects.filter(name__icontains=q)

    return render(request, "index.html", {
        "products": products,
        "query": q
    })


def live_search(request):
    query = request.GET.get("q", "")

    if not query:
        return JsonResponse({"products": []})

    products = Product.objects.filter(name__icontains=query)[:8]

    data = []

    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "image": product.image.url if product.image else ""
        })

    return JsonResponse({
        "products": data
    })