""" Custom Login view """
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login

from .NotLoggedRequiredMixin import NotLoggedRequiredMixin
from django.shortcuts import redirect

class CustomLoginView(NotLoggedRequiredMixin,LoginView):
    template_name = 'authentication/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        if form.errors:
            messages.error(self.request, message=form.errors,
                           extra_tags="danger")

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        return super(CustomLoginView, self).form_valid(form)

        # # Check if user have detailed profile
        # if user.person:
        #     user_first_name = user.person.first_name
        #     msg = "Olá "+user_first_name+", você foi logado com sucesso"
        #     messages.success(self.request, message=msg, extra_tags="success")
        #     return super(CustomLoginView, self).form_valid()
        # else:
        #     registration_url = reverse('home')
        #     #user_email = user.email
        #     return HttpResponseRedirect(registration_url)

