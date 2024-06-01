from django.shortcuts import render,redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url="/login_page/")
def receipe(request):
   
    if request.method=="POST":

        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        recepie_description=data.get('recepie_description')
        
        """ print(receipe_name)
        print(recepie_description)
        print(receipe_image) """
        Reciepe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            recepie_description=recepie_description
        )
        return redirect('/receipe/')
    Queryset=Reciepe.objects.all()
    context={'recipes':Queryset,'page': 'receipe'}
    return render(request,"receipe.html",context)
@login_required(login_url="/login_page/")
def delete_reciepe(request,id):
    recipe = Reciepe.objects.get(id=id)
    recipe.delete()
    return redirect('receipe') 

@login_required(login_url="/login_page/")
def update_reciepe(request,id):
    recipes = Reciepe.objects.get(id=id)
    #to save the updated data in the db
    if request.method =="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        recepie_description=data.get('recepie_description')

        recipes.receipe_name=receipe_name
        recipes.recepie_description=recepie_description
        if receipe_image:
            recipes.receipe_image=receipe_image
        recipes.save()
        return redirect('receipe') 

    context={'receipe':recipes,'page':"update_reciepe"}
    return render(request,"update_reciepe.html",context) 


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        # Authenticate using the custom user model
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request,'Invalid Username or Password')
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('receipe') 
            
    return render(request,'login.html',context={'page':'Login Page'})

        
            
        
#request is used to load static data on the browser

def logout_page(request):
    logout(request)
    return redirect('login_page')




def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')  # Assuming you have a 'username' field in your registration form
        password=request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('register')

        # Create a new user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        # Set the password
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")
        return redirect('login_page')

    return render(request,'register.html',context={'page':'Register Page'})

def Hello(request):
    return HttpResponse("Hello! This is a Recipe APP")