from loguru import logger

from django.contrib.auth.models import User
from django.views.generic import DetailView

from django.shortcuts import redirect, render

from accounts.models import Account

# Create your views here.
def register_view(request):
    if request.method == 'POST':
          try:
               username = request.POST.get('username')
               email = request.POST.get('email')
               password = request.POST.get('password')

               user = User(username=username, email=email)
               user.set_password(password)
               user.save()

               account = Account(user=user)
               account.save()
               return redirect('login')

          except Exception as e:
               logger.error(f"Error while creating user {e}")
               return redirect('register')

    return render(request=request, template_name='account/register_account.html')


class AccountDetailView(DetailView):
     model = Account
     template_name = 'account/account.html'
     context_object_name = 'account'
