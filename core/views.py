from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from .models import Timetable, Task, Resource
from .forms import TimetableForm, TaskForm, ResourceForm, RegisterForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')



def home(request):
    # Redirect to dashboard if user is logged in
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        # Otherwise, show the login page
        from django.contrib.auth.views import LoginView
        return LoginView.as_view(template_name='core/login.html')(request)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'core/login.html'


@login_required
def timetable_edit(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk, user=request.user)
    if request.method == 'POST':
        timetable.subject = request.POST['subject']
        timetable.day = request.POST['day']
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')
        timetable.save()
        return redirect('timetable')
    return render(request, 'core/timetable_edit.html', {'timetable': timetable})

@login_required
def timetable(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        day = request.POST['day']
        start_time = request.POST.get('start_time')
        end_time= request.POST.get('end_time')
        Timetable.objects.create(user=request.user, subject=subject, day=day, start_time=start_time,end_time=end_time)
    
        return redirect('timetable')
    timetables = Timetable.objects.filter(user=request.user)
    return render(request, 'core/timetable.html', {'timetables': timetables})


@login_required
def timetable_delete(request, pk):
    item = get_object_or_404(Timetable, pk=pk, user=request.user)
    item.delete()
    return redirect('timetable')



@login_required
def delete_timetable(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == "POST":
        timetable.delete()
        return redirect('timetable')
@login_required
def tasks(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        if title:
            Task.objects.create(user=request.user, title=title, due_date=due_date)
        return redirect('tasks')

    user_tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'core/tasks.html', {'tasks': user_tasks})


@login_required
def task_toggle(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks')


@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('tasks')
    return render(request, 'core/task_edit.html', {'task': task})

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('tasks')


@login_required
def resources(request):
    if request.method == "POST":
        title = request.POST.get('title')
        file = request.FILES.get('file')
        image = request.FILES.get('image')
        link = request.POST.get('link')
        Resource.objects.create(title=title, file=file, image=image, link=link, user=request.user)
        return redirect('resources')

    resources = Resource.objects.filter(user=request.user)
    return render(request, 'core/resources.html', {'resources': resources})

@login_required
def resource_delete(request, id):
    resource = get_object_or_404(Resource, id=id, user=request.user)
    resource.delete()
    return redirect('resources')

@login_required
def dashboard(request):
    from datetime import date, timedelta
    today = date.today()
    upcoming_tasks = Task.objects.filter(user=request.user, due_date__gte=today, completed=False).order_by('due_date')[:5]
    today_timetable = Timetable.objects.filter(user=request.user, day=today.strftime('%A')).order_by('start_time')
    return render(request, 'core/dashboard.html', {
        'upcoming_tasks': upcoming_tasks,
        'today_timetable': today_timetable,
    })
