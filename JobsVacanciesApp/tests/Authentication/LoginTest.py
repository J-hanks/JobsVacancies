from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from JobsVacanciesApp.tests.SeleniumHelpers import fillInputMaskedElement, SeleniumStaticServernMixin

import time


class LoginTest(SeleniumStaticServernMixin):
    fixtures = [
        "WebUserAdm.json",
    ]

    def setUp(self):
        # SetupManager()
        super(LoginTest, self).setUp()

        #self.page_url = "http://127.0.0.1:8000/register_merchant"
        self.page_url = self.live_server_url+reverse('login')

        self.selenium.get(self.page_url)

    def tearDown(self):
        # Clean up run after every test method.
        self.selenium.quit()
        pass

    def test_login_and_logout(self):
        # Assert Login Title
        self.assertIn(_("Access your account"), self.selenium.page_source)

        self.selenium_login_adm()
        # assert home page
        self.assertIn(self.live_server_url, self.selenium.current_url)

        self.selenium_logout()

        # assert login page
        self.assertIn(self.page_url, self.selenium.current_url)
