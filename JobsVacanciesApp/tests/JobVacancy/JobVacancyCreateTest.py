from django.urls import reverse


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import fillInputMaskedElement, SeleniumStaticServernMixin
from JobsVacanciesApp.models import WebUser, JobVacancy, Company
import time


class JobVacancyCreateTest(SeleniumStaticServernMixin):

    def setUp(self):
        # SetupManager()
        super(JobVacancyCreateTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url+reverse('JobVacancyCreateView')
        self.company_create_url = self.live_server_url + \
            reverse('CompanyCreateView')
        self.job_vacancy_list_url = self.live_server_url + \
            reverse('JobVacancyListView')

        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        time.sleep(10)
        self.selenium.quit()
        pass

    def test_create_vacancy(self):
        # Test Login Required
        self.assertIn(self.login_url, self.selenium.current_url)

        self.selenium_login_webuser()

        # Test Company Required
        self.assertIn(self.company_create_url, self.selenium.current_url)
        company_name = "Test Company"
        name_field = self.selenium.find_element_by_id('id_name')
        name_field.send_keys(company_name)
        submit_btn = self.selenium.find_element_by_id('id_submit_btn')
        submit_btn.click()
        test_company = Company.objects.get(name=company_name)
        self.assertIn(self.page_url, self.selenium.current_url)


        #create vacancy
        vacancy_name = "Test Vacancy"
        vacancy_salary_range = JobVacancy.salary_range_over_three
        vacancy_minimun_education = JobVacancy.minimum_education_high_school
        vacancy_requisites = "Lorem i..."
      
      
        name_field = self.selenium.find_element_by_id('id_name')
        salary_range_field = Select(self.selenium.find_element_by_id('id_salary_range'))
        minimun_education_field = Select(self.selenium.find_element_by_id('id_minimum_education'))
        requisites_field = self.selenium.find_element_by_id('id_requisites')

        
        name_field.send_keys(vacancy_name)
        salary_range_field.select_by_value(vacancy_salary_range)
        minimun_education_field.select_by_value(vacancy_minimun_education)
        requisites_field.send_keys(vacancy_requisites)
        self.submitForm()
        job_vacancy = JobVacancy.objects.get(name=vacancy_name)
        self.assertIn(self.job_vacancy_list_url, self.selenium.current_url)
        
        # Remove Vacancy
        remove_btn = self.selenium.find_element_by_id(f"id_job_vacancy_{job_vacancy.pk}_remove_btn")
        remove_btn.click()
        
        vacancy_delete_url = self.live_server_url + \
            reverse("JobVacancyDeleteView", kwargs={'pk': job_vacancy.pk})
        self.assertIn(vacancy_delete_url, self.selenium.current_url)
        remove_btn = self.selenium.find_element_by_id(f"id_remove_btn")
        remove_btn.click()
        self.assertIn(self.job_vacancy_list_url, self.selenium.current_url)
        
        job_vacancy, created = JobVacancy.objects.get_or_create(
            name=vacancy_name,
            salary_range =vacancy_salary_range,
            minimum_education =vacancy_minimun_education,
            requisites =vacancy_requisites,
            company=test_company
        )
        self.assertTrue(created)

        #Test Detail






        # Assert Login Title
        # username = "test@testemail.com"
        # password = "JobConvo123*"
        # username_field = self.selenium.find_element_by_id('id_email')
        # password1_field = self.selenium.find_element_by_id('id_password1')
        # password2_field = self.selenium.find_element_by_id('id_password2')
#
#
        # username_field.send_keys(username)
        # password1_field.send_keys(password)
        # password2_field.send_keys(password)
        # assert login page after logout
