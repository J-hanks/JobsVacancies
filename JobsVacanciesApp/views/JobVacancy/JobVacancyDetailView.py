from django.views.generic import DetailView
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from JobsVacanciesApp.models import JobVacancy
from JobsVacanciesApp.forms import JobApplicationForm


class JobVacancyDetailView(LoginRequiredMixin, DetailView):
    model = JobVacancy
    context_object_name = "job_vacancy"
    template_name = "JobVacancy/JobVacancyDetail.html"
    methods = ("get", "post")
    form_class = JobApplicationForm

    def post(self, request, *args, **kwargs):
        jobApplicationForm = self.form_class(
            request.POST, prefix='jobApplicationForm')
        if jobApplicationForm.is_valid():
            jobApplication = jobApplicationForm.save(commit=False)
            jobApplication.user = request.user
            jobApplication.job_vacancy = self.get_object()
            jobApplication.save()
            messages.add_message(request, messages.SUCCESS, _(
                "Your application was send. Thank you. Now you should hire Joao, my creator."))
        else:
            print("INVALID")

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["userApplied"] = None
        context["userOwnVacancy"] = True if self.get_object().company == self.request.user.company else False
        try:
            context["userApplied"] = True if self.get_object(
            ).jobapplication_set.get(user=self.request.user) else False
        except:
            pass
        if self.request.POST:
            context['jobApplicationForm'] = JobApplicationForm(
                self.request.POST, prefix='jobApplicationForm')
        else:
            context['jobApplicationForm'] = JobApplicationForm(
                prefix='jobApplicationForm')
        return context
