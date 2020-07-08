from django.urls import path
from .import views

urlpatterns = [
    path('',views.create_view,name='create_view'),
    path('list/',views.list_view,name='list_view'),
]
