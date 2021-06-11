from django.urls import reverse


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import SeleniumStaticServernMixin
from JobsVacanciesApp.models import WebUser, JobVacancy, Company, JobApplication
import time


class JobApplicationDeleteTest(SeleniumStaticServernMixin):

    def setUp(self):
        # SetupManager()
        super(JobApplicationDeleteTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url+reverse('JobApplicationListView')
        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        # time.sleep(10)
        self.selenium.quit()
        pass

    def test_delete_application(self):
        # Test Login Required
        self.assertIn(self.login_url, self.selenium.current_url)

        self.selenium_login_webuser()

        self.assertIn(self.page_url, self.selenium.current_url)

        # # Remove Vacancy
        job_application = JobApplication.objects.filter(
            user__email=self.webuser_email).first()
        remove_btn = self.selenium.find_element_by_id(
            f"id_job_application_{job_application.pk}_remove_btn")
        remove_btn.click()

        job_application_delete_url = self.live_server_url + \
            reverse("JobApplicationDeleteView",
                    kwargs={'pk': job_application.pk})

        self.assertIn(job_application_delete_url, self.selenium.current_url)
        self.submitForm()
        self.assertIn(self.page_url, self.selenium.current_url)
