from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.list_categories_ordered, name='list_categories_ordered'),  
    path('categories/create/', views.create_category, name='create_category'),  
    path('categories/update/<int:id>/', views.update_category, name='update_category'),  
    path('categories/delete/<int:id>/', views.delete_category, name='delete_category'),  

]