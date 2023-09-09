import csv, json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, DeleteTaskForm,UpdateTaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('show_task')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def show_task(request):
    tasks = Task.objects.filter(User= request.user)
    form = TaskForm(request.GET)
    status = request.GET.get('status')
    sort = request.GET.get('sort')

    if status == '1':
        tasks = tasks.filter(Completed=True)
    elif status == '0':
        tasks = tasks.filter(Completed=False)

    
    if sort:
        tasks = tasks.order_by(sort)
    return render(request, 'show_tasks.html', {'tasks': tasks, 'form': form})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.User = request.user
            task.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request, 'show_tasks.html', {'form': form})
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = UpdateTaskForm(request.POST or None, instance=task)
    return render(request, 'update_tasks.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = DeleteTaskForm(request.POST, instance=task)
        if form.is_valid():
            task.delete()
            return redirect('show_task')
    else:
        form = DeleteTaskForm(instance=task)
    return render(request, 'show_tasks.html', {'form': form, 'task': task})


def download_task_csv(request):
    tasks = Task.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="task.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Creation Date', 'Status'])

    for task in tasks:
        writer.writerow(
            [task.Title, task.Description, task.Created_at, 'Completed' if task.Completed else 'Not Completed'])

    return response

def download_task_json(request):
    tasks = Task.objects.all()

    task_data = []

    for task in tasks:
        task_dict = {
            'Title': task.Title,
            'Description': task.Description,
            'Creation Date': task.Created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'Status': 'Completed' if task.Completed else 'Not Completed'
        }
        task_data.append(task_dict)

    json_data = json.dumps(task_data, indent=4)

    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="tasks.json"'

    return response
