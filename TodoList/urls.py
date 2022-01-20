from django.urls import include,path
from . import views
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('', views.todoList, name='todo'),
    path('todo-list', views.todoList, name='ToDoList' ),
    path('add-todo', views.add_todo, name='add_todo'),
    path('delete/<str:pk>', views.delete_todo, name='delete_todo'),
    path('completed/<str:pk>', views.complete_todo, name='complete_todo'),
    path('incompleted/<str:pk>', views.incomplete_todo, name='incomplete_todo'),
    path('auth', views.auth, name='authentication'),
    path('reg-user', views.reg_user, name='registration'),
    path('signout', views.signout, name='signout'),


    #email Verification
    path('email/',include(mail_urls)),
    path('send_email/',views.sendEmail),

]