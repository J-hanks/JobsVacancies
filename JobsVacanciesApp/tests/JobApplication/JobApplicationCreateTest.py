from django.urls import reverse


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import SeleniumStaticServernMixin
from JobsVacanciesApp.models import WebUser, JobVacancy, Company, JobApplication
import time


class JobApplicationCreateTest(SeleniumStaticServernMixin):

    def setUp(self):
        # SetupManager()
        super(JobApplicationCreateTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url + \
            reverse('JobVacancyDetailView', kwargs={'pk': 3})
        self.job_application_list_url = self.live_server_url + \
            reverse('JobApplicationListView')

        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        # time.sleep(10)
        self.selenium.quit()
        pass

    def test_create_application(self):
        # Test Login Required
        self.assertIn(self.login_url, self.selenium.current_url)

        self.selenium_login_webuser()

        self.assertIn(self.page_url, self.selenium.current_url)

        # create application
        application_pay_claim = JobVacancy.salary_range_over_three
        application_last_education = JobVacancy.minimum_education_high_school
        application_experience = "Lorem i..."

        pay_claim_field = Select(self.selenium.find_element_by_id(
            'id_jobApplicationForm-pay_claim'))
        last_education_field = Select(self.selenium.find_element_by_id(
            'id_jobApplicationForm-last_education'))
        experience_field = self.selenium.find_element_by_id(
            'id_jobApplicationForm-experience')

        pay_claim_field.select_by_value(application_pay_claim)
        last_education_field.select_by_value(application_last_education)
        experience_field.send_keys(application_experience)
        self.submitForm()
        self.assertIn(self.page_url, self.selenium.current_url)
        self.assertTrue(JobApplication.objects.get(
            user__email=self.webuser_email, job_vacancy__pk=3))
