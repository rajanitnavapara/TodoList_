from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo-list', views.todoList, name='ToDoList' ),
    path('add-todo', views.add_todo, name='add_todo'),
    path('delete/<str:pk>', views.delete_todo, name='delete_todo'),
    path('completed/<str:pk>', views.complete_todo, name='complete_todo'),
    path('incompleted/<str:pk>', views.incomplete_todo, name='incomplete_todo'),

]