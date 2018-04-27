from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fight/', views.fight, name='fight'),
    path('shop/', views.shop, name='shop'),
]
