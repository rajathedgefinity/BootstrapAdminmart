from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.login_user,name="login"),
    path('logout/', views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('dashboard/',views.home,name="dashboard"),
]
