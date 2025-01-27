from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def resgiter_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'auth_app/register.html'
    context = {'form':form}
    return render(request, template_name, context)


def login_view(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        u = request.POST['un']
        p = request.POST['pw']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('todo_show')
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('register')
