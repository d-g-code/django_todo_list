from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    return render(request, 'todo/index.html', {'todo_list': todo_list, 'form': form})


def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')
