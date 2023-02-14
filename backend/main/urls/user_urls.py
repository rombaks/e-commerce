from django.urls import path

from main.views.user_views import (
    MyTokenObtainPairView,
    get_user,
    get_users,
    register_user,
)


urlpatterns = [
    path("", get_users, name="users"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", get_user, name="user"),
    path("register/", register_user, name="register"),
]
