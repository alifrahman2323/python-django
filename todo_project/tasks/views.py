from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import TaskForm

def create_task(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create_task')

    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})