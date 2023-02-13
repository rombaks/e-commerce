from django.urls import path

from main.views import (
    MyTokenObtainPairView,
    get_product,
    get_products,
    get_user,
    get_users,
    register_user,
)


urlpatterns = [
    path("products/", get_products, name="products"),
    path("products/<str:pk>", get_product, name="product"),
    path("users/register/", register_user, name="register"),
    path("users/profile/", get_user, name="user"),
    path("users/", get_users, name="users"),
    path("users/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
