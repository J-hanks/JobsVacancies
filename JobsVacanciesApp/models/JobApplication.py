from django.db import models
from django.utils.translation import ugettext as _
from .TimeStampedModelMixin import TimeStampedModelMixin
from .WebUser import WebUser
from .JobVacancy import JobVacancy


class JobApplication(TimeStampedModelMixin):

    job_vacancy = models.ForeignKey(JobVacancy, verbose_name=_(
        "Job Vacancy"), on_delete=models.CASCADE)

    user = models.ForeignKey(WebUser, verbose_name=_(
        "User"), on_delete=models.CASCADE)

    pay_claim = models.CharField(
        _("Pay claim"), choices=JobVacancy.salary_range_choices, max_length=255)

    last_education = models.CharField(
        _("Last education"), choices=JobVacancy.minimum_education_choices, max_length=255)

    experience = models.TextField(_("Experience"))
    # Experiência

    class Meta:
        unique_together = [['job_vacancy','user']]
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'
    def __str__(self):
        return f"{self.job_vacancy} - {self.user}"
