from django.urls import path
from .  import views

urlpatterns = [
    path('', views.list_post, name="list_post"),
    path('post/<int:pk>/', views.view_post, name='view_post'),
    path('post/new/', views.add_post, name='add_post'), 
    path('post/<int:pk>/edit/', views.edit_post,name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
