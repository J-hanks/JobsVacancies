from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from JobsVacanciesApp.models import JobApplication

class JobApplicationDeleteView(DeleteView):
    model = JobApplication
    template_name = "JobApplication/JobApplicationDelete.html"
    success_url = reverse_lazy('JobApplicationListView')