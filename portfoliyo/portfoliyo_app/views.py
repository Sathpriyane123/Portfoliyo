from django.shortcuts import render

from.models import *

# Create your views here.

# home page
def home(request):
    return render(request, "index1.html")

# cotact form

def contact(request):
    emp={}
    try:
        name= request.POST['name']
        email= request.POST['email']
        description= request.POST['description']
        form= Contact.objects.create(name=name, email=email, description=description)
        form.save()
        return render(request, 'index1.html',emp)
    except Exception as b:
        print(b)
        emp['key']= 'not submited'
        return render(request,'index1.html',emp)


