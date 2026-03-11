from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from apps.shop.models import Product


@login_required
def add_review(request, product_id):

    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST["rating"]
        text = request.POST["text"]
        Review.objects.update_or_create(

            user=request.user,
            product=product,

            defaults={
                "rating": rating,
                "text": text
            }

        )

    return redirect(f"/product/{product_id}")