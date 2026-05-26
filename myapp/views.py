from django.shortcuts import render
from .models import Forms

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        Forms.objects.create(name=name,age=age,dob=dob)
    return render(request,"form.html")

def result(request):
    result=Forms.objects.all()
    return render(request,"result.html",{"result":result})

def formedit(request):
    return render(request,"formedit.html")
