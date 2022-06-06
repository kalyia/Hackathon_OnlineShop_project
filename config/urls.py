from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('apps.account.urls')),
    path('api/v1/category/', include('apps.category.urls')),
    path('api/v1/product/', include('apps.product.urls')),
    path('api/v1/shoppingcart/', include('apps.cart.urls')),
    path('api/v1/', include('apps.order.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
