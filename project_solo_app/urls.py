from django.urls import path
from . import views
urlpatterns = [
    #localhost:8000/dreams
    path('', views.index), 
    #localhost:8000/dreams/new
    path('new', views.new), 
    #localhost:8000/dreams/create
    path('create', views.create),
    #localhost:8000/dreams/<dream_id>/edit
    path('<int:dream_id>/edit', views.edit), 
    #localhost:8000/dreams/<dream_id>/update
    path('<int:dream_id>/update', views.update),
    #localhost:8000/dreams/<dream_id>
    path('<int:dream_id>', views.dream),
    #localhost:8000/dream/<dream_id>/delete
    path('<int:dream_id>/delete', views.delete),

]