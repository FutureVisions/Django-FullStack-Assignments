from django.urls import path
from . import views
urlpatterns = [
    path('all', views.all_show),
    path('delete/<int:id>', views.delete),
    path('create/show', views.create_show),
    path('create', views.create),
    path('show/<int:id>', views.one_show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
]
