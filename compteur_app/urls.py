from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter_view, name='counter'),
    path('increment/', views.increment, name='increment'),
    path('decrement/', views.decrement, name='decrement'),
]
