from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserCreationForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def logout_view(request):
    logout(request)
    return redirect('Inicio') 


def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio')  # Redirige a la vista de inicio
        msg_login = "Usuario o contraseña incorrectos"
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request): 
    msg_register = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirige al login después del registro exitoso
        else:
            msg_register = "Error en los datos ingresados"
    else:
        form = UserCreationForm()

    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})


@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return render(request, "myapp1/index.html")
        else:
            # Si el formulario no es válido, renderiza la misma página con errores
            return render(request, "users/editar_usuario.html", {"form": formulario})
    else:
        formulario = UserEditForm(instance=usuario)
    
    # Renderiza la página de edición con el formulario
    return render(request, "users/editar_usuario.html", {"form": formulario})


class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy("EditarUsuario")