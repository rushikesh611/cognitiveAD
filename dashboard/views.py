from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/authentication/login')
def homeview(request):
    return render(request,'index.html')

def index(request):
    return render(request,'dashboard/index.html')

def tools(request):
    return render(request,'dashboard/tools.html')