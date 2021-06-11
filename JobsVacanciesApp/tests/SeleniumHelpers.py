from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from django.utils.translation import ugettext as _

from django.shortcuts import reverse
import time



def fillInputMaskedElement(element, value):
    element.click()
    for digit in value:
        element.send_keys(Keys.HOME, digit)
        time.sleep(0.3)


class SeleniumStaticServernMixin(StaticLiveServerTestCase):
    fixtures = [
        "WebUserAdm.json",
        "WebUser.json",
        "Companies.json",
        "JobsVacancies.json",
        "JobsApplications.json",
    ]
    
    webuser_email = "webuser@jobsvacancies.com"
    webuser_password = "jobsvacancies"

    webuser_adm_email = "adm@jobsvacancies.com"
    webuser_adm_password = "jobsvacancies"

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.login_url = self.live_server_url+reverse('login')

        super(SeleniumStaticServernMixin, self).setUp()

    def tearDown(self):
        # Clean up run after every test method.
        self.selenium.quit()
        super(SeleniumStaticServernMixin, self).tearDown()

    def selenium_login(self, username, password):
        #self.login_url = self.live_server_url+reverse('login')
        # self.selenium.get(self.login_url)
        username_field = self.selenium.find_element_by_id('id_username')
        password_field = self.selenium.find_element_by_id('id_password')
        submit_btn = self.selenium.find_element_by_id('id_submit_btn')
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()

    def selenium_login_webuser(self):
        self.selenium_login(self.webuser_email,
                            self.webuser_password)

    def selenium_login_adm(self):
        self.selenium_login(self.webuser_adm_email,
                            self.webuser_adm_password)

    def submitForm(self):
        submit_btn = self.selenium.find_element_by_id('id_submit_btn')
        submit_btn.click()

    def selenium_logout(self):
        # test logout
        auth_bar_btn = self.selenium.find_element_by_id(
            'authenticationBarButton')
        auth_bar_btn.click()

        logout_btn = self.selenium.find_element_by_id('logout_btn')
        logout_btn.click()
        self.assertIn(self.login_url, self.selenium.current_url)
