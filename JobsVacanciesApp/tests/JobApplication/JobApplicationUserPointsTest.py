from django.urls import reverse


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import SeleniumStaticServernMixin
from JobsVacanciesApp.models import WebUser, JobVacancy, Company, JobApplication
import time


class JobApplicationUserPointsTest(SeleniumStaticServernMixin):

    def setUp(self):
        # SetupManager()
        super(JobApplicationUserPointsTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url + \
            reverse('JobVacancyDetailView', kwargs={'pk': 1})
        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        # time.sleep(10)
        self.selenium.quit()
        pass

    def test_create_application(self):
        # Test Login Required
        self.assertIn(self.login_url, self.selenium.current_url)

        self.selenium_login_webuser_company()

        self.assertIn(self.page_url, self.selenium.current_url)

        points_field = self.selenium.find_element_by_id(
            'id_job_application_1_user_points')
        #First application should have 0 points
        self.assertEqual(points_field.text , "0")
        
        #Second application should have 2 points
        points_field = self.selenium.find_element_by_id(
            'id_job_application_2_user_points')
        self.assertEqual(points_field.text , "2")

        #Third application should have 1 points
        points_field = self.selenium.find_element_by_id(
            'id_job_application_3_user_points')
        self.assertEqual(points_field.text , "1")


        #Fourth application should have 1 points
        points_field = self.selenium.find_element_by_id(
            'id_job_application_4_user_points')
        self.assertEqual(points_field.text , "1")


