from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index Page</h1> <a href='/todo-list'>ToDo List</a>")

def todoList(request):
    todo1 = Todo()
    todo1.id = 1
    todo1.name = 'Aadhar'
    todo1.priority = 1

    todo2 = Todo()
    todo2.id = 2
    todo2.name = 'Pancard'
    todo2.priority = 2
    
    todo3 = Todo()
    todo3.id = 3
    todo3.name = 'Django'
    todo3.priority = 4
    
    todo4 = Todo()
    todo4.id = 4
    todo4.name = 'RND'
    todo4.priority = 3
    
    todo5 = Todo()
    todo5.id = 5
    todo5.name = 'College'
    todo5.priority = 5
    
    #storing all todo in one list
    # todos = [todo1,todo2,todo3,todo4,todo5]
    todos = Todo.objects.all()
    # print(todos[0].priority)
    # sorted_todos = sorted(x,key=lambda x:x[1])
    # print(sorted_todos)
    #sorting all todo according to their priority
    # print(todos.sort(key=lambda x: x.priority, reverse=False))
    return render(request,'todos.html',{'todos':todos})
    # return HttpResponse('Todo : ',todo1.name)

def add_todo(request):
    if request.method == 'POST':
        todo = Todo()
        todo.name = request.POST['todo-name']
        todo.priority = request.POST['priority']
        
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
    todo.priority = Todo.objects.filter(id=pk)[0].priority
    # print(Todo.objects.filter(id=pk)[0].completed)     
    todo.save()

    # print(Todo.objects.filter(id=pk)[0].completed)     
    todos = Todo.objects.all()
    return redirect('/todo-list')
    # return redirect('/todo-list')        
     