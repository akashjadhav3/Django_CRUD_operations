from django.urls import path
from .import views

urlpatterns = [
    path('',views.create_view,name='create_view'),
    path('list/',views.list_view,name='list_view'),
    path('detail/<id>',views.detail_view,name='detail_view'),
    path('update/<id>',views.update_view,name='update_view'),
    path('delete/<id>',views.delete_view,name='delete_view'),
]
