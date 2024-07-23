from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:pk>/', views.show_image, name='show_image'),
]
