from django.urls import path
from .views import product_list, product_detail


app_name = 'shopapp'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:slug>', product_list, name='product_list_by_category'),
    path('<int:id>', product_detail, name='product_detail')
]