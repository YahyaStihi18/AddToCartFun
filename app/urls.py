from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "app"

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('checkout/',views.checkout,name='checkout'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('add-to-cart/<pk>/',views.add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name='remove-from-cart'),
    path('add/<int:pk>',views.add,name='add'),
    path('remove/<int:pk>',views.remove,name='remove'),


    path('register/', views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name='app/logout.html'),name='logout' ),


]
