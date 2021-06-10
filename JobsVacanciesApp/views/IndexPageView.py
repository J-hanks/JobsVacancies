from django.views.generic import TemplateView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from JobsVacanciesApp.models import JobVacancy


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs_vacancies"] = JobVacancy.objects.all()
        return context
