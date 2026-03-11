from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),

    path('search/', views.search, name='search'),

    path('live-search/', views.live_search, name='live_search'),
]