from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
def all_show(request):
    context = {
        "show": Show.objects.all()
    }
    return render(request, 'all_show.html', context)

def create(request):
    return render(request, 'new_show.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create')
    new_show=Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        date=request.POST['date'],
        desc=request.POST['desc']
        )
    return redirect(f'/show/{new_show.id}')

def one_show(request, id):
    context = {
        "one_show": Show.objects.get(id=id)
    }
    return render(request, "show.html", context)

def edit(request, id):
    context = {
        'edit': Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

def update(request, id):
    errors = Show.objects.update_validator(request.POST)
    show=Show.objects.get(id=id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{show.id}')
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.date=request.POST['date']
    show.desc=request.POST['desc']
    show.save()
    return redirect(f'/show/{show.id}')

def delete(request, id):
    dele=Show.objects.get(id=id)
    dele.delete()
    return redirect('/all')

# Create your views here.
