from typing import Tuple
from time import sleep

import selene
from selene import have, command

from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, modal, date
from tests.test_data.users import Subject
from demoqa_tests.utils import path
import allure
from allure_commons.types import Severity


class LoginPage:
    def __init__(self, browser: selene.Browser):
        self.browser = browser

    def given_opened(self):
        self.browser.open("https://www.codewars.com/")
        return self

    @allure.step("Залогинится")
    def login(self, username, password):
        self.browser.element("#login-btn").click()

        self.browser.element("#user_email").send_keys(username)
        self.browser.element("#user_password").send_keys(password)
        self.browser.element("//button").should(have.text("Sign in")).click()

