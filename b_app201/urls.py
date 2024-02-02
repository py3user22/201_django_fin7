from django.urls import path
from . import views


urlpatterns = [
    path('', views.home1, name="home1"),
    path('home', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    # path('bookings/', views.bookings, name="bookings"),
    # path('book/', views.book, name="book"),
]
