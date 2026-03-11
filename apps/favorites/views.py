from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from apps.shop.models import Product


@login_required
def favorites_page(request):

    favorites = Favorite.objects.filter(user=request.user)
    products = [fav.product for fav in favorites]

    return render(request, "favorites.html", {
        "products": products
    })


@login_required
def toggle_favorite(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    favorite = Favorite.objects.filter(
        user=request.user,
        product=product
    ).first()

    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(
            user=request.user,
            product=product
        )

    return redirect(request.META.get("HTTP_REFERER", "/"))