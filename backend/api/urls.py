from django.conf.urls import url, include
from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^Logic/$', ReactAppView.as_view(template_name='index.html'), name='Logic'),
    path("hello/", HelloAPI),
    path("info/<str:id>", ItemAPI, name="get_info"),
    path("price/<str:id>", PriceAPI, name="get_price"),
    path("price/<str:id>/update", UpdateAPI.as_view(), name="update_item"),
    path("price/<str:id>/delete", DeleteAPI.as_view(), name="delete_item"),
    #path("", ReactAppView.as_view()),
    path("shopping/<str:id>", ShoppingCartAPI, name="shopping_cart"),
    path("object_detect/", ObjectDetectAPI, name="object_detect"),
]
