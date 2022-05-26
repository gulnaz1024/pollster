from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path("login/", views.login_request, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)