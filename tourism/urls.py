from django.urls import path
from .import views

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('',views.home,name='home'),
  
]


#   path('sabarimala/',views.sabarimala,name='sabarimala'),
#     path('anjumala/',views.anjumala,name='anjumala'),
#     path('aranmula/',views.aranmula,name='aranmula'),
#     path('charalkkunnu/',views.charalkkunnu,name='charalkkunnu'),
#     path('chengara/',views.chengara,name='chengara'),
#     path('chuttippara/',views.chuttippara,name='chuttippara'),
#     path('gavi/',views.gavi,name='gavi'),
#     path('konniadavi/',views.konniadavi,name='konniadavi'),
#     path('mannera/',views.mannera,name='mannera'),
#     path('nilakkal/',views.nilakkal,name='nilakkal'),
#     path('orakkanpara/',views.orakkanpara,name='orakkanpara'),
#     path('pandalam/',views.pandalam,name='pandalam'),
#     path('parumala/',views.parumala,name='parumala'),
#     path('perunthenaruvi/',views.perunthenaruvi,name='perunthenaruvi'),