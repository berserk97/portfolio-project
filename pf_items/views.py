from django.shortcuts import render
from .models import Project
from .models import Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'pf_items/home.html', {'projects': projects, 'skills': skills})



