from django.shortcuts import render
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'todoapp/index.html', context)

from django.shortcuts import get_object_or_404, redirect

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(title=title, description=description)
        todo.save()
        return redirect('todo_list')
    return render(request, 'todoapp/add.html')


def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('todo_list')
    context = {'todo':todo}
    return render(request, 'todoapp/update.html', context)
