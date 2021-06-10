""" perso_required_mixin.py """

from django.views import View
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

from JobsVacanciesApp.models import Company

# Class Based View Mixin To check
# if user has Person Object associated with account


class CompanyRequiredMixin(View):
    """ Requires and authenticated user with person object assossiated """

    def dispatch(self, request, *args, **kwargs):
        company = request.user.company
        # Try to get person object, This is nedded because
        # Django uses anonymous user object when user not logged in
        # and AnonymousUser Object does not have person attribute, raising an error
        if company:
            return super().dispatch(request, *args, **kwargs)
        else:
            # If person not found redirect to the page for create one
            return redirect("CompanyCreateView")
