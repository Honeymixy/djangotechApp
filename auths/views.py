from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
# Login Function    
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {user}')
            return redirect('home')
    context = {'form': form}
    
    return render(request, 'register.html', context)
    
    
# # def loginPage(request):
# #     if request.method == 'POST':
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #         user = authenticate(request, username=username, password=password)
# #         if user is not None:
# #             login(request, user)
# #             return redirect('home')
# #         else:
# #             messages.info(request, 'username OR password is not correct')
        
        
        
# #     return render(request, 'login.html')

# def logoutPage(request):
#     logout(request)
#     messages.success(request, ('You have been logged out....'))
#     return redirect('login')

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get['username']
#         password = request.POST.get['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have been logged in successfully...')
#             return redirect('home')
#         else:
#             messages.info(request, 'username OR password is not correct')
#     return render(request, 'login.html', {})
        