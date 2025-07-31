from django.urls import reverse
from loguru import logger

from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.models import Account

# Create your views here.
def register_view(request):
    if request.method == 'POST':
          try:
               username = request.POST.get('username')
               email = request.POST.get('email')
               ##TODO: Hash password
               password = request.POST.get('password')
               user = User(username=username, email=email, password=password)
               user.save()

               account = Account(user=user)
               account.save()
               return redirect('login')

          except Exception as e:
               logger.error(f"Error while creating user {e}")
               return redirect('register')

    return render(request=request, template_name='register_account.html')



# # Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#           try:
#                email = request.POST.get('email')
#                ##TODO: Hash password
#                password = request.POST.get('password')

#                user = User.objects.get(email=email)
#                if user.password == password:
#                     return render(request=request, template_name='account.html')
#                else:
#                     ##TODO: Handle Error
#                     return render(request=request, template_name='login.html')
#           except Exception as e:
#                logger.info(f"Error while creating user {e}")
#                return

#     return render(request=request, template_name='login.html')
