from django.urls import path
from . import views

urlpatterns = [
    path('', views.icecream_list),
    path('<int:pk>/', views.icecream_detail),
]
