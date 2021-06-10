from django.db import models
from django.utils.translation import ugettext as _
from .TimeStampedModelMixin import TimeStampedModelMixin
from django.urls import reverse
from .Company import Company


class JobVacancy(TimeStampedModelMixin):

    # COMPANY FIELD
    # JobVacancy Belongs to Company
    company = models.ForeignKey(
        Company, verbose_name=_("Company"), on_delete=models.CASCADE)

    # NAME FIELD
    name = models.CharField(_("Name"), max_length=255)

    # SALARY RANGE FIELD
    salary_range_up_one = "up_one"
    salary_range_from_one_to_two = "from_one_to_two"
    salary_range_from_two_to_three = "from_two_to_three"
    salary_range_over_three = "over_three"

    salary_range_choices = (
        (salary_range_up_one, _("Up to 1,000")),
        (salary_range_from_one_to_two, _("From 1,000 to 2,000")),
        (salary_range_from_two_to_three, _("From 2,000 to 3,000")),
        (salary_range_over_three, _("Over 3,000")),
    )

    salary_range = models.CharField(
        _("Salary Range"), choices=salary_range_choices, max_length=255)

    # MINIMUM EDUCATION FIELD
    minimum_education_elementary_school = "1"
    minimum_education_high_school = "2"
    minimum_education_technical = "3"
    minimum_education_higher_Education = "4"
    minimum_education_mba = "5"
    minimum_education_phd = "6"

    minimum_education_choices = (
        (minimum_education_elementary_school, _("Ensino fundamental")),
        (minimum_education_high_school, _("Ensino médio")),
        (minimum_education_technical, _("Tecnólogo")),
        (minimum_education_higher_Education, _("Ensino Superior")),
        (minimum_education_mba, _("Pós / MBA / Mestrado")),
        (minimum_education_phd, _("Doutorado")),
    )

    minimum_education = models.CharField(
        _("Minimum Education"), choices=minimum_education_choices, max_length=255)

    requisites = models.TextField(_("Requisites"))

    def applicationsCount(self):
        return self.jobapplication_set.all().count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('JobVacancyDetailView', kwargs={'pk': self.pk})
