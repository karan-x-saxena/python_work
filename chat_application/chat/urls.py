from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('<str:space>/',views.space,name='space'),
    path('checkspace',views.checkspace,name='checkspace'),
    path('send',views.send,name='send'),
    path('getMessages/<str:space>/',views.getMessages,name='getMesssages'),
    path('logout',views.logout,name='logout'),
]
