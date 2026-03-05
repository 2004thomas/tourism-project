from django.urls import path
from .import views

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('place/<int:place_id>/gallery/',views.gallery,
    name='gallery'),
    path('place/<int:place_id>/reviews/',views.reviews,
    name='reviews'),
    path('',views.home,name='home'),
  
]
