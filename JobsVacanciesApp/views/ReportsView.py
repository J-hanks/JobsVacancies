from django.views.generic import TemplateView

from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Count

from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from JobsVacanciesApp.models import JobVacancy, JobApplication

from chartjs.views.lines import BaseLineChartView
import calendar


class MonthlyChartView(BaseLineChartView):

    years = None
    years_array = []

    months = None
    months_array = [_("January"), _("February"), _("March"), _("April"), _("May"), _("June"), _(
        "July"), _("August"), _("September"), _("October"), _("November"), _("December"), ]

    data = []
    object_class = None

    def __init__(self, *args, **kwargs):
        self.data = []
        self.years_array = []

        self.years = self.object_class.objects.annotate(
            year=TruncYear('create_date')).values('year')

        for year in self.years:
            self.years_array.append(year['year'].year)

        self.years_array = list(set(self.years_array))
        print()

        for year in self.years_array:
            year_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.months = JobVacancy.objects.filter(create_date__year=year).annotate(month=TruncMonth(
                'create_date')).values('month').annotate(counter=Count('id')).values('month', 'counter')
            for month in self.months:
                year_data[month['month'].month - 1] = month['counter']
            self.data.append(year_data)

        return super().__init__(*args, **kwargs)

    def get_labels(self):
        return self.months_array

    def get_providers(self):
        """Return names of datasets."""
        return self.years_array

    def get_data(self):
        """Return 3 datasets to plot."""
        return self.data


class MonthlyVacanciesChartView(MonthlyChartView):
    object_class = JobVacancy


class MonthlyApplicationsChartView(MonthlyChartView):
    object_class = JobApplication


class ReportsView(TemplateView):
    template_name = "reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs_vacancies"] = JobVacancy.objects.all()

        return context
