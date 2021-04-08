from django.urls import path
from . import views
app_name = 'shop'
urlpatterns=[
    path(r'shop/',views.product_list,name='product_list'),
    path(r'shop/(?P<category_slug>[-\w]+)/',views.product_list,name='product_list_by_category'),
    path(r'shop/(?P<id>\d+)/(?P<slug>[-\w]+)/',views.product_detail,name='product_detail')
]
