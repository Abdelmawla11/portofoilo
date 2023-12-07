from django.shortcuts import render
from .models import *

def home(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        data = Message(name=name,email=email,message=message)
        data.save()
    
    context = {
        'me' : Me.objects.all(),
        'link' : Link.objects.all(),
        'skills' : Skill.objects.all(),
        'photo' : Photo.objects.all(),
        'video' : Video.objects.all(),
        'meta' : Meta.objects.all()
    }    
    return render(request , 'portfolio/index.html', context)
