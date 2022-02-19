from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    count = User.objects.count()
    return render(
        request,
        'home.html',
        {'count': count}
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(
        request,
        'registration/signup.html',
        {'form': form}
    )


@login_required
def secret_page(request):
    users = User.objects.all()
    ckeckbox_list = request.POST.getlist("selected_options")
    if request.POST.get('blockbtn'):
        for user in ckeckbox_list:
            us = User.objects.get(id=user)
            us.is_active = False
            us.save()
        return render(
            request,
            'admin_page.html',
            {'users': users}
        )
    elif request.POST.get('unblockbtn'):
        for user in ckeckbox_list:
            us = User.objects.get(id=user)
            us.is_active = True
            us.save()
        return render(
            request,
            'admin_page.html',
            {'users': users}
        )
    elif request.POST.get('delbtn'):
        try:
            for user in ckeckbox_list:
                us = User.objects.get(id=user)
                us.delete()
        except Exception as e:
            print(e)
        return render(
            request,
            'admin_page.html',
            {'users': users}
        )
    else:
        return render(
            request,
            'admin_page.html',
            {'users': users}
        )


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'admin_page.html'
