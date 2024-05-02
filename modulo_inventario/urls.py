from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products_list/", views.product_list, name="products_list"),
    path("products_create/", views.product_create, name="products_create"),
    path("products_delete/<int:product_id>", views.product_delete, name="products_delete"),
    path("products_update/<int:product_id>", views.product_update, name="products_update")
]
