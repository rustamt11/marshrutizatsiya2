from django.urls import path
from . import views

app_name = 'factory1'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
