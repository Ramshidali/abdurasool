from . import views
from django.urls import path, re_path

# Create your tests here.

app_name = 'product'

urlpatterns = [
    path('category/', views.category_view, name='category'),
    re_path(r'^category-view/(?P<pk>.*)/$', views.category_single_view, name='category_single'),
    re_path(r'^create-category/$', views.create_category_view, name='create_category'),
    re_path(r'^edit-category/(?P<pk>.*)/$', views.edit_category_view, name='edit_category'),
    re_path(r'^delete-category/(?P<pk>.*)/$', views.delete_category_view, name='delete_category'),


    path('product/', views.product_view, name='product'),
    re_path(r'^product-view/(?P<pk>.*)/$', views.product_single_view, name='product_single'),
    re_path(r'^create-product/$', views.create_product_view, name='create_product'),
    re_path(r'^edit-product/(?P<pk>.*)/$', views.edit_product_view, name='edit_product'),
    re_path(r'^delete-product/(?P<pk>.*)/$', views.delete_product_view, name='delete_product'),
]