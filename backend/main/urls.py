from django.urls import path

from main.views import (
    MyTokenObtainPairView,
    get_product,
    get_products,
    get_routes,
    get_user,
    get_users,
)


urlpatterns = [
    path("", get_routes, name="routes"),
    path("products/", get_products, name="products"),
    path("products/<str:pk>", get_product, name="product"),
    path("users/profile/", get_user, name="user"),
    path("users/", get_users, name="users"),
    path("users/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
