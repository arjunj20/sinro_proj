from django.urls import path
from .views import ProductList, ProductDetail
from .views import product_list

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('', product_list, name='product-list-page'),
]

