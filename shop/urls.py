from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.get_product_list, name='product_list'),
    path('products/<str:products_slug>/', views.get_product_detail, name='product_detail')
]