from django.urls import path
from . import views

urlpatterns = [
    path("", views.orders_list),
    path("create/", views.create_order),
    path("<int:order_id>/", views.order_detail),
]