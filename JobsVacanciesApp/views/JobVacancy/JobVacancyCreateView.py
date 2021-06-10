from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from JobsVacanciesApp.views import CompanyRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

from JobsVacanciesApp.models import JobVacancy


class JobVacancyCreateView(LoginRequiredMixin, CompanyRequiredMixin, CreateView):
    model = JobVacancy
    template_name = "JobVacancy/JobVacancyCreate.html"
    fields = ("name", "salary_range", "minimum_education", "requisites")

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.company = self.request.user.company
        vacancy.save()
        messages.add_message(self.request, messages.SUCCESS, _(
                "Vacancy added. Thank you. Now you should hire Joao, my creator."))
        return redirect("JobVacancyListView")
