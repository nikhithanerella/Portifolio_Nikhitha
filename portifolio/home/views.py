from django.shortcuts import render
from home.models import contact
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def projects(request):
    return render(request,'projects.html')
def web(request):
    return render(request,'web.html')
def back(request):
    return render(request,'back.html')
def frame(request):
    return render(request,'frame.html')
def contact_me(request):
    if request.method=="POST":
        name=request.POST['name'] 
        email=request.POST['email'] 
        phone=request.POST['phone'] 
        address=request.POST['address'] 
         
        ins=contact(name=name,email=email,phone=phone,address=address)
        ins.save()
         
    
    return render(request,'contact.html')
