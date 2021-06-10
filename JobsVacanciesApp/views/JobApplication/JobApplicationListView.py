from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from JobsVacanciesApp.models import JobApplication


class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    context_object_name = 'JobApplications'
    template_name = "JobApplication/JobApplicationList.html"

    def get_queryset(self):
        queryset = JobApplication.objects.filter(user=self.request.user)
        return queryset
