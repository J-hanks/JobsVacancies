from django.views.generic import View
from django.shortcuts import redirect


# Class Based View Mixin To check 
# if user has Person Object associated with account
class NotLoggedRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return redirect("home")
        else:
            return super(NotLoggedRequiredMixin,self).dispatch(request, *args, **kwargs)