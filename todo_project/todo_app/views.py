from django.shortcuts import render, redirect
from .forms import TodoForm, Todo


def todo_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo_show')
    template_name = 'todo_app/todo_form.html'
    context = {'form':form}
    return render(request, template_name, context)

def show_view(request):
    obj = Todo.objects.all()
    template_name = 'todo_app/todo_show.html'
    context = {'data':obj}
    return render(request, template_name, context)

def update_view(request, pk):
    obj = Todo.objects.get(id=pk)
    form =TodoForm(instance=obj)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('todo_show')
    template_name = 'todo_app/todo_form.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_view(request, pk):
    obj = Todo.objects.get(id=pk)
    obj.delete()
    return redirect('todo_show')

