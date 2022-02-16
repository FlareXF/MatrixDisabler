from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт был создан для {username}! Теперь вы можете войти в аккаунт')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'name': cut_name(request)
    }
    return render(request , 'users/register.html', context)

def personal(request):
    return render(request, 'users/personal.html')
    
def change(request):
    return render(request, 'users/change.html')

def trahnut(request):
    return render(request, 'users/trahnut.html')

def delete(request):
    return render(request, 'users/delete.html')


@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    context = {
        'u_from': u_form,
        'p_form': p_form,
        'name': cut_name(request)
    }
    return render(request, 'users/profile.html', context)


def cut_name(request):
    nameuser = request.user.username
    if len(nameuser) > 10:
        return (nameuser[:8] + '..')