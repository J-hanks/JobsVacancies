from django.views.generic.edit import UpdateView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from JobsVacanciesApp.views import CompanyRequiredMixin

from JobsVacanciesApp.models import JobVacancy


class JobVacancyUpdateView(LoginRequiredMixin, CompanyRequiredMixin, UpdateView):
    model = JobVacancy
    template_name = "JobVacancy/JobVacancyUpdate.html"
    fields = ("name", "salary_range", "minimum_education", "requisites")
