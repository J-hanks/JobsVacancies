from django.urls import reverse


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import fillInputMaskedElement, SeleniumStaticServernMixin
from JobsVacanciesApp.models import WebUser
import time


class SignUpTest(SeleniumStaticServernMixin):
    fixtures = [
        "WebUserAdm.json",
    ]

    def setUp(self):
        # SetupManager()
        super(SignUpTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url+reverse('signup')
        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        # time.sleep(10)
        self.selenium.quit()
        pass

    def test_signup(self):
        # Assert Login Title
        self.assertIn(_("Create an account"), self.selenium.page_source)
        username = "test@testemail.com"
        password = "JobConvo123*"
        username_field = self.selenium.find_element_by_id('id_email')
        password1_field = self.selenium.find_element_by_id('id_password1')
        password2_field = self.selenium.find_element_by_id('id_password2')
        submit_btn = self.selenium.find_element_by_id('id_submit_btn')


        username_field.send_keys(username)
        password1_field.send_keys(password)
        password2_field.send_keys(password)
        submit_btn.click()
        # assert home page
        self.assertIn(self.live_server_url, self.selenium.current_url)

        self.selenium_logout()
        self.assertTrue(WebUser.objects.get(email = username))
        # assert login page after logout
        self.assertIn(self.login_url, self.selenium.current_url)
