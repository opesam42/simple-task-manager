from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # tasks = Tasks.objects.all().values()
    tasks = Tasks.objects.filter(author_id=request.user.id).values()
    print(tasks)
    return render(request, 'tasks/home.html', {'tasks':tasks, 'user':request.user})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.author = request.user #assign authorship to login user
            tasks.save() #save to database
            return redirect('tasks:home')
    else:
        form = TaskForm()

    return render(request, 'tasks/add.html', {'form':form,})