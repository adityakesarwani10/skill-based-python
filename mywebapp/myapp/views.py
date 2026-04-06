from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import MyTable 

# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def test(request):
    return HttpResponse("This is the test page.")

def show(request):
    return HttpResponse("Now we have understand the concept of url mapping...")

def abcd(request):
    return HttpResponse("Abcd Page")

def show_name(request):
    return HttpResponse("Aditya kesarwani \n DOB: 09-01-2005")

def index(request):
    return render(request,'index.html')

def testing(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing2(request): 
    template = loader.get_template('All_members.html')
    return HttpResponse(template.render())

def submit(request):
    template = loader.get_template('submit.html')
    return HttpResponse(template.render())
    
def number(request):
    members = {1,2,3,4,5,6,7,8,9,10}
    return render(request, 'number.html', {'members': members})

def insert_data(request):
    # return render(request, 'form.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        try:
            MyTable.objects.create(name=name, subject=subject, email=email)
            messages.success(request, 'Data inserted successfully!')
        except IntegrityError as e:
            messages.error(request, f'Error inserting data: {str(e)}')
            return render(request, 'form.html', {'error': str(e)})
        return redirect('form.html')  # Redirect to a success page after insertion
    
    return render(request, 'form.html')

def values(request):
    mymembers = MyTable.objects.all().values()

    template = loader.get_template('All_members.html')

    context = {
        "members" : mymembers
    }
    return HttpResponse(template.render(context, request))

