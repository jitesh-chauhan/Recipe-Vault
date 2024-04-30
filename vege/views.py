from django.shortcuts import render, redirect, get_object_or_404
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# for creating receipes
@login_required(login_url='/login_page/')
def recipes(request):
    if request.method=='POST':
        
        data= request.POST
        recipe_img=request.FILES['recipe_img']
        recipe_name=data.get('recipe_name')
        
        recipe_description=data.get('recipe_description')
        
        recipe.objects.create(
            recipe_name= recipe_name,
            recipe_img=recipe_img,
            recipe_description=recipe_description
        )
        return redirect('/recipes/')
    
    recipe_data=recipe.objects.all() 
    
    # for searching receipes
    if request.GET.get("search"):
       recipe_data=recipe_data.filter(recipe_name__icontains=request.GET.get("search")) 
        
        
    context={'recipes':recipe_data}  
    return render(request, 'recipes.html',context )

 # for deleting receipes
@login_required(login_url='/login_page/')
def del_recipe(request, id):
    queryset = get_object_or_404(recipe, id=id)
  
    queryset.delete()
  
    return redirect('/recipes/')


@login_required(login_url='/login_page/')
def update_recipe(request,id):
    queryset=recipe.objects.get(id=id)
    if request.method=='POST':
        recipe_name=request.POST.get('recipe_name')
        recipe_description=request.POST.get('recipe_description')
       
        recipe_img=request.FILES['recipe_img']
    
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if recipe_img:
            queryset.recipe_img=recipe_img
        queryset.save()
        return redirect('/recipes/')
    
    recipe_data=recipe.objects.all()
    context={'recipe':recipe_data}
    return render(request,'update.html',context)    


def login_page(request):
    if request.method=='POST':
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        
        if User.objects.filter(username = username).exists():
           
    
            user=authenticate(username=username, password=password)
    
            if user is None:
                messages.error(request, "Invalid username or password")
                return redirect("/login_page/")
            else:
                login(request,user)
                return redirect("/recipes/")
        else:
            messages.error(request, "Invalid username!")
            return redirect("/login_page/")
    
      
    return render(request, 'login.html', { 'is_login_page':True })

def logout_page(request):
    logout(request)
    return redirect("/login_page/")




def register_page(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        password=data.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return redirect('/register/')
         
            
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created succcesfully')
        return redirect('/login_page/')
    return render(request,'register.html')    

