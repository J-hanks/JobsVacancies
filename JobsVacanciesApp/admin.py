from django.contrib import admin

from JobsVacanciesApp.models import Company

from JobsVacanciesApp.models import WebUser
from JobsVacanciesApp.models import JobApplication
from JobsVacanciesApp.models import JobVacancy


# Register your models here.
admin.site.register(Company)
admin.site.register(WebUser)
admin.site.register(JobApplication)
admin.site.register(JobVacancy)
