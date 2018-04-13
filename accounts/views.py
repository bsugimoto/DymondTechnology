from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import SignUpForm, UserInformationUpdateForm, ProfileForm, ProfileInformationUpdateForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            form2.save()
            user = form.save()
            user.refresh_from_db()
            form2 = ProfileForm(request.POST, request.FILES, instance=user.profile)
            form2.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        form2 = ProfileForm()
    return render(request, 'signup.html', {'form':form, 'form2': form2})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserInformationUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileInformationUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserInformationUpdateForm(instance=request.user)
        profile_form = ProfileInformationUpdateForm(instance=request.user.profile)
    return render(request, 'my_account.html', {'user_form': user_form,'profile_form': profile_form})
