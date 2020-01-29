from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('dashboard/',views.home,name="dashboard"),
]
