from django.urls import path

from main.views.product_views import get_product, get_products


urlpatterns = [
    path("", get_products, name="products"),
    path("<str:pk>/", get_product, name="product"),
]
