from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



class UserRegistorView(View):
    def get(self, request):
        return render(request, 'log_tem/registor.html')
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        replay_password = request.POST['replay_password']
        if password == replay_password:
            user = User(first_name=first_name, last_name= last_name, email=email, username=username)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'log_tem/registor.html')
            
                
    
class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'log_tem/index.html', {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        data = {
            'username': username,
            'password' : password
        }

        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        
        else:
            form = UserLoginForm()
            context={
                'form':form
            }
            return render(request, 'log_tem/registor.html', context)
        
class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    