from django.views.generic import DetailView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from JobsVacanciesApp.models import Company


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "Company/CompanyDetail.html"
