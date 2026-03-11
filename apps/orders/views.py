from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from apps.cart.models import CartItem


@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        return redirect("/cart")

    total = sum(item.total_price() for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect("/orders")


@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, "orders.html", {
        "orders": orders
    })


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, "order_detail.html", {
        "order": order
    })