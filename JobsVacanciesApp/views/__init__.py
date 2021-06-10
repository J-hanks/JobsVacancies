from .authentication import CustomLoginView, CustomSignUpView, CustomLogoutView, CompanyRequiredMixin, CustomSignUpView
from .IndexPageView import IndexPageView

from .Company import CompanyDetailView, CompanyCreateView
from .JobVacancy import JobVacancyDetailView, JobVacancyListView, JobVacancyCreateView, JobVacancyDeleteView, JobVacancyUpdateView
from .JobApplication import JobApplicationListView, JobApplicationDeleteView


from .ReportsView import ReportsView, MonthlyApplicationsChartView, MonthlyVacanciesChartView


