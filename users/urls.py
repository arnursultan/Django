from django.urls import path
from users import views

urlpatterns = [
    path("users/register/", views.UserRegister.as_view(), name="register"),
]