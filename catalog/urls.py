from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, products_detail

app_name = CatalogConfig.name

urlpatterns = [path("", home, name="base"),
               path("contacts/", contacts, name="contacts"),
               path("products_list/", products_list, name="products_list"),
               path("products_detail/<int:pk>/", products_detail, name="products_detail"), ]
