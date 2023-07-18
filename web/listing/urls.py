from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('scrape/<scrape_id>', views.list_flats, name='scrape'),
]
