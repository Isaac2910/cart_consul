
# authentication/views.py

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms


#from django.contrib.auth import login, authenticate· # import des fonctions login et authenticate



def login_page(request):

    form = forms.LoginForm()

    message = ''

    if request.method == 'POST':

        form = forms.LoginForm(request.POST)

        if form.is_valid():

            user = authenticate(

                username=form.cleaned_data['username'],

                password=form.cleaned_data['password'],

            )

            if user is not None:

                login(request, user)

                message = f'Bonjour, {user.username}! Vous êtes connecté.'

            else:

                message = 'Identifiants invalides.'

    return render(

        request, 'authentification/login.html', context={'form': form, 'message': message})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')