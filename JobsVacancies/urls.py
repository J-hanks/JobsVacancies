"""JobsVacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from JobsVacanciesApp.views import CustomLoginView, CustomSignUpView, CustomLogoutView, IndexPageView
from JobsVacanciesApp.views import CompanyDetailView, CompanyCreateView

from JobsVacanciesApp.views import JobApplicationListView, JobApplicationDeleteView
from JobsVacanciesApp.views import JobVacancyListView, JobVacancyCreateView, JobVacancyDetailView, JobVacancyUpdateView, JobVacancyDeleteView
from JobsVacanciesApp.views import ReportsView, MonthlyApplicationsChartView, MonthlyVacanciesChartView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name="IndexPageView"),
    path('', IndexPageView.as_view(), name="home"),
    path('', IndexPageView.as_view(), name="contact"),

    path('signup', CustomSignUpView.as_view(), name='signup'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # JOB VACANCIES
    path('MyVacancies', JobVacancyListView.as_view(),
         name='JobVacancyListView'),
    
    path('NewVacancy', JobVacancyCreateView.as_view(),
         name='JobVacancyCreateView'),

    path('UpdateVacancy/<int:pk>', JobVacancyUpdateView.as_view(),
         name='JobVacancyUpdateView'),
    
    path('Vacancy/<int:pk>', JobVacancyDetailView.as_view(),
         name='JobVacancyDetailView'),
    
    path('RemoveVacancy/<int:pk>', JobVacancyDeleteView.as_view(),
         name='JobVacancyDeleteView'),



    # COMPANY
    path('NewCompany', CompanyCreateView.as_view(),
         name='CompanyCreateView'),
    path('Company/<int:pk>', CompanyDetailView.as_view(), name='CompanyDetailView'),


    # APPLICATIONS
    path('MyApplications', JobApplicationListView.as_view(),
         name='JobApplicationListView'),
    path('CancelApplication/<int:pk>', JobApplicationDeleteView.as_view(),
         name='JobApplicationDeleteView'),


    # REPORTS
    path('Reports', ReportsView.as_view(),
         name='ReportsView'),
    path('MonthlyApplicationsChartView', MonthlyApplicationsChartView.as_view(),
         name='MonthlyApplicationsChartView'),
    path('MonthlyVacanciesChartView', MonthlyVacanciesChartView.as_view(),
         name='MonthlyVacanciesChartView'),



]
