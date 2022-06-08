from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('', views.home),
    path('email/', views.email),
    path('em/',views.email1),
    path('comp/',views.compose),
    path('lan/',views.Language),
    path('fon/',views.myfunction),
    # path('',views.hi)

]