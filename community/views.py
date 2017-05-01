from django.shortcuts import render
from .models import Project, Event, Category, PDFContent, VideoContent
from django.views.decorators.clickjacking import xframe_options_exempt


def index(request):
    c = {}
    c['title'] = 'comunidade de programação'
    c['oi'] = 'oi'
    c['explanation'] = 'O projeto “comunidade de programação” visa alavancar a aprendizagem de programação de jovens e adultos através de abordagens democráticas, e explorar maneiras de tornar a programação acessível a um público numeroso e diverso usando e-learning.'
    return render(request, "index.html", c)


def categories(request):
    c ={}
    c['title'] = 'comunidade de programação'
    c['categories'] = Category.objects.all()
    return render(request, "categories.html", c)


@xframe_options_exempt
def video_content(request, id):
    c ={}
    c['content'] = VideoContent.objects.get(id=id)
    c['type'] = 'video'
    c['title'] = 'comunidade de programação'
    return render(request, "content.html", c)


@xframe_options_exempt
def pdf_content(request, id):
    c ={}
    c['content'] = PDFContent.objects.get(id=id)
    c['type'] = 'pdf'
    c['title'] = 'comunidade de programação'
    return render(request, "content.html", c)


def contents(request, id):
    c ={}
    c['pdfs'] = PDFContent.objects.filter(category__id=id)
    c['videos'] = VideoContent.objects.filter(category__id=id)
    c['title'] = 'comunidade de programação'
    return render(request, "contents.html", c)


def projects(request):
    c ={}
    c['title'] = 'comunidade de programação'
    c['projects'] = Project.objects.all()
    return render(request, "projects.html", c)


def events(request):
    c ={}
    c['title'] = 'comunidade de programação'
    c['events'] = Event.objects.all()
    return render(request, "events.html", c)