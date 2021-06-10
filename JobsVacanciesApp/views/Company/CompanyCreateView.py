from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from JobsVacanciesApp.models import Company


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "Company/CompanyCreate.html"
    fields = ("name",)

    def form_valid(self, form):
        company = form.save()
        self.request.user.company = company
        self.request.user.save()
        return redirect("JobVacancyCreateView")