from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_pembayaran, name='create_pembayaran'),
    path('list/', views.list_pembayaran, name='list_pembayaran'),
    path('update/<int:id>/', views.update_pembayaran, name='update_pembayaran'),
    path('delete/<int:id>/', views.delete_pembayaran, name='delete_pembayaran'),
]
