from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import *

# Authentication imports
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def error(request):
    return render(request, '404.html')
def details(request):
    return render(request, 'blog-details.html')
def blog(request):
    return render(request, 'blog.html')
def index(request):
    if request.method == 'POST':
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')



def portfolio(request):
    return render(request, 'portfolio-details.html')
def service(request):
    return render(request, 'service-details.html')
def starter(request):
    return render(request, 'starter-page.html')
def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', {"all" : all})

def delete(request, id):
    contactinfo = Contact.objects.get(id=id)
    contactinfo.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)

    if request.method == "POST" :
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.subject = request.POST.get('subject')
        editappointment.message = request.POST.get('message')
        editappointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html',{'editappointment':editappointment})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    return render(request, 'login.html')