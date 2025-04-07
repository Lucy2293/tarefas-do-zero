from django.urls import path
from .views import *

urlpatterns = [
    path('tasks' , listar, name='listar-view'),
    path('tasks/<int:task_id>' , update, name='edicao') ,
    ]
