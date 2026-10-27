from django.urls import path
from .views import post_list, post_detail, post_create, post_delete, post_edit

urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:pk>', post_detail, name='post_detail'),
    path('create', post_create, name='post_create'),
    path('delete/<int:pk>', post_delete, name='post_delete'),
    path('edit/<int:pk>', post_edit, name='post_edit'),
]