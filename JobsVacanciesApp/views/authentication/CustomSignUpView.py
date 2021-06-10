# Create your views here.
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.contrib import messages
from django.shortcuts import render

from JobsVacanciesApp.models import WebUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .NotLoggedRequiredMixin import NotLoggedRequiredMixin


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = WebUser
        fields = ("email", "password1",)


class CustomSignUpView(NotLoggedRequiredMixin, CreateView):
    model = WebUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'authentication/signup.html'

    def post(self, request, *args, **kwargs):
        user_form = CustomUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:

            messages.error(request, message=user_form.errors,
                           extra_tags="danger")

            return render(request, 'authentication/signup.html', {'form': user_form})
