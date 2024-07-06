from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def logar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("username")
            senha = form.cleaned_data.get("password")

            user = authenticate(username=login, password=senha)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Usuário inválido.")


    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})