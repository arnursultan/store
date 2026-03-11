from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.shop.urls')),
    path('cart/', include('apps.cart.urls')),
    path('favorites/', include('apps.favorites.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('orders/', include('apps.orders.urls')),
    path('users/', include('apps.users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)