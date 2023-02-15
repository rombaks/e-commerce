from django.urls import path

from main.views.user_views import (
    MyTokenObtainPairView,
    get_user,
    get_users,
    register_user,
    update_user,
)


urlpatterns = [
    path("", get_users, name="users"),
    path("register/", register_user, name="register"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", get_user, name="user"),
    path("profile/update/", update_user, name="update"),
]
