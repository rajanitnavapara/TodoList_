
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# from EmailVerification.views import sendEmail
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_email_verification import send_email

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index Page</h1> <a href='/todo-list'>ToDo List</a>")
usernm = ""

@login_required(login_url='/auth')
def todoList(request):
    # todo1 = Todo()
    # todo1.id = 1
    # todo1.name = 'Aadhar'
    # todo1.priority = 1

    # todo2 = Todo()
    # todo2.id = 2
    # todo2.name = 'Pancard'
    # todo2.priority = 2
    
    # todo3 = Todo()
    # todo3.id = 3
    # todo3.name = 'Django'
    # todo3.priority = 4
    
    # todo4 = Todo()
    # todo4.id = 4
    # todo4.name = 'RND'
    # todo4.priority = 3
    
    # todo5 = Todo()
    # todo5.id = 5g 
    # todo5.name = 'College'
    # todo5.priority = 5
    
    #storing all todo in one list
    # todos = [todo1,todo2,todo3,todo4,todo5]

    # print(todos[0].priority)
    # sorted_todos = sorted(x,key=lambda x:x[1])
    # print(sorted_todos)
    #sorting all todo according to their priority
    # print(todos.sort(key=lambda x: x.priority, reverse=False))
    username = request.user.username
    todos = Todo.objects.filter(user=username)
    return render(request,'todos.html',{'todos':todos,'username': username})
    # return HttpResponse('Todo : ',todo1.name)
@login_required(login_url='/auth')
@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        todo = Todo()
        todo.name = request.POST['todo-name']
        todo.priority = request.POST['priority']
        todo.user = request.user.username
        # todo.user = User
        todo.save() 
        # print(Todo.name,'todo added')
        return redirect('/todo-list')
    else:
        return redirect('/todo-list')

@csrf_exempt
def delete_todo(request,pk):
    Todo.objects.filter(id=pk).delete()
    return redirect('/todo-list')

@csrf_exempt
def complete_todo(request,pk):

    # Todo.objects.filter(id=pk).completed = 1
    # print(Todo.objects.filter(id=pk)[0].completed)       
    # print('complete')
    todo = Todo()
    todo.name = Todo.objects.filter(id=pk)[0].name
    todo.id = Todo.objects.filter(id=pk)[0].id
    todo.user = request.user.username
    todo.completed = True 
    todo.priority = Todo.objects.filter(id=pk)[0].priority
    # print(Todo.objects.filter(id=pk)[0].completed)     
    todo.save()
    # print(Todo.objects.filter(id=pk)[0].completed)     
    todos = Todo.objects.all()
    # print('updated')
    return redirect('/todo-list')
    # return render(request,'todos.html',{'todos':todos})
    # return HttpResponse('Done')

@csrf_exempt
def incomplete_todo(request,pk):
   
    # Todo.objects.filter(id=pk).completed = 1
    # print(Todo.objects.filter(id=pk)[0].completed) 
    # print('incomplete')
    todo = Todo()
    todo.name = Todo.objects.filter(id=pk)[0].name
    todo.id = Todo.objects.filter(id=pk)[0].id
    todo.completed = False 
    todo.user = request.user.username
    todo.priority = Todo.objects.filter(id=pk)[0].priority
    # print(Todo.objects.filter(id=pk)[0].completed)     
    todo.save()

    # print(Todo.objects.filter(id=pk)[0].completed)     
    todos = Todo.objects.all()
    return redirect('/todo-list')
    # return redirect('/todo-list')        
     

#register User
def reg_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.create_user(username=username,password=password)
        # user.save()
        sendEmail()
        return redirect('/auth')
    return render(request,'sign_up.html')

@csrf_exempt
def sendEmail(request):
    # if request.method == 'POST':
    password = request.POST['password']
    username = request.POST['username']
    email = request.POST['email']
    user = get_user_model().objects.create(username=username,password=password,email=email)
    user.is_active = False
    # user = User.objects.create(username=username,password=password,email=email)
    send_email(user)
    return render(request,'EmailVerification/confirm_template.html')

    
#authentication
@csrf_exempt
def auth(request):
    if request.method == "POST":
        username = request.POST['username']
        usernm = username
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print("user: ",user)
        if user is not None:
            login(request, user)
            todos = Todo.objects.all()
            # return render(request,'todos.html',{'username':user,'todos':todos})
            return redirect('/todo-list')
        else:
            # print('user not found')
            # print(user)
            return render(request,'sign_in.html',{'user_not_found': True,'username':username})
    return render(request,'sign_in.html')


#Signing Out
def signout(request):
    logout(request)
    return render(request,'sign_in.html',{'msg': 'You are sign out.'})