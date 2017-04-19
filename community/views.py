from django.shortcuts import render


def index(request):
    c = {}
    c['title'] = 'comunidade de programação'
    c['explanation'] = 'O projeto “comunidade de programação” visa alavancar a aprendizagem de programação de jovens e adultos através de abordagens democráticas, e explorar maneiras de tornar a programação acessível a um público numeroso e diverso usando e-learning.'
    return render(request, "index.html", c)