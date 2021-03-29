from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Game

# Create your views here.
# @login_required(login_url='/authentication/login')
def homeview(request):
    return render(request,'index.html')

def index(request):
    return render(request,'dashboard/index.html')

def tools(request):
    tools = Game.objects.all()
    context = { 'tools' : tools }
    return render(request,'dashboard/tools.html', context)

def levelview(request, gametype):
    tools = Game.objects.all()
    tool = Game.objects.filter(gametype = gametype).first()
    context = { 
        'tools' : tools,
        'tool' : tool
    }
    return render(request,'dashboard/levelpage.html', context)

def reactiontimeone(request):
    return render(request,'dashboard/reactiontime1.html')

def reactiontimetwo(request):
    return render(request,'dashboard/reactiontime2.html')

def memoryone(request):
    return render(request,'dashboard/memory1.html')

def memorytwo(request):
    return render(request,'dashboard/memory2.html')

def spatialmemoryone(request):
    return render(request,'dashboard/spatialmemory1.html')

def pairedalmazeone(request):
    return render(request,'dashboard/pairedalMaze1.html')

def pairedalmazetwo(request):
    return render(request,'dashboard/pairedalMaze2.html')

def rapidvisualone(request):
    return render(request,'dashboard/rapidvisual1.html')

def reactiontwo(request):
    return render(request,'dashboard/reactiontimeg2.html')

def motorone(request):
    return render(request,'dashboard/motor1.html')



