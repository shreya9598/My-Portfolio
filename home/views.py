from django.shortcuts import render, HttpResponse
from home.models import Contact 

# Create your views here.
def home(request):
    context = {'name': 'Shreya', 'course': 'Django'}    #using variables
    return render(request, 'home.html', context)        #using template

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']

        contact = Contact(name=name, email=email, phone=phone, desc= desc)
        contact.save()           #to save in database

    return render(request, 'contact.html')

