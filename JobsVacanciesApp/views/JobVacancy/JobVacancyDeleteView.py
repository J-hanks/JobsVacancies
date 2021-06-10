from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from JobsVacanciesApp.models import JobVacancy


class JobVacancyDeleteView(DeleteView):
    model = JobVacancy
    template_name = "JobVacancy/JobVacancyDelete.html"
    success_url = reverse_lazy('JobVacancyListView')
