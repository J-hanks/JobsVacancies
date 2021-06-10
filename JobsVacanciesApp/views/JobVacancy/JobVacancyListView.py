from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from JobsVacanciesApp.models import JobVacancy
from JobsVacanciesApp.views import CompanyRequiredMixin


class JobVacancyListView(LoginRequiredMixin, CompanyRequiredMixin, ListView):
    model = JobVacancy
    context_object_name = 'JobVacancies'
    template_name = "JobVacancy/JobVacancyList.html"

    def get_queryset(self):
        queryset = JobVacancy.objects.filter(company=self.request.user.company)
        return queryset
