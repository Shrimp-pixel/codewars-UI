import os
from time import sleep

from demoqa_tests.model import app
from demoqa_tests.model.pages.login_page import LoginPage
from tests.test_data.users import yuri
from demoqa_tests.utils import attach
import allure


def test_login(setup_browser):
    username = os.getenv('CODEWARS_LOGIN')
    password = os.getenv('CODEWARS_PASSWORD')

    LP = LoginPage(setup_browser)
    LP.login(username, password)

#    browser.element('#submit').click()
