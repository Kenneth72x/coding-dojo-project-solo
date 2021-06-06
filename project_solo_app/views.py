from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dream


def index(request):
    context = {
        'dreams': Dream.objects.all()
    }
    return render(request, 'dreams.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    #Create the dream
    errors = Dream.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/project_solo_app/new')    
    Dream.objects.create(
        title = request.POST['title'], 
        mood = request.POST['mood'],
        dream_date = request.POST['dream_date'],
        description = request.POST['description']
    )
    return redirect('/project_solo_app')    

def edit(request, dream_id):
    one_dream = Dream.objects.get(id=dream_id)
    context = {
        'dream': one_dream
    }
    return render(request, 'edit.html', context)

def update(request, dream_id):
    errors = Dream.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/project_solo_app/{dream_id}/edit') 
    #update dream!
    to_update = Dream.objects.get(id=dream_id)
    #update each field
    to_update.title = request.POST['title']
    to_update.dream_date = request.POST['dream_date']
    to_update.mood = request.POST['mood']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/project_solo_app')

def dream(request, dream_id):
    #query for one dream with dream_id
    one_dream = Dream.objects.get(id=dream_id)
    context = {
        'dream': one_dream
    }
    return render(request, 'dream.html', context)

def delete(request, dream_id):
    #note: delete one dream!
    to_delete = Dream.objects.get(id=dream_id)
    to_delete.delete()
    return redirect('/project_solo_app') 
# Create your views here.
