from django.urls import path

from main.views import (
    MyTokenObtainPairView,
    get_product,
    get_products,
    get_routes,
    get_user,
)


urlpatterns = [
    path("", get_routes, name="routes"),
    path("products/", get_products, name="products"),
    path("products/<str:pk>", get_product, name="product"),
    path("users/profile/", get_user, name="user"),
    path("users/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
