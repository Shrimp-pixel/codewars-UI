import os
from codewars_tests.model.pages.codewarspage import CodeWarsPage
from selene import have
from tests.test_data.users import newUser
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка сайта Codewars')
@allure.story("Проверка логин")
@allure.link('https://www.codewars.com/', name='Testing')
def test_login(setup_browser):
    email = newUser.email
    password = newUser.password

    LP = CodeWarsPage(setup_browser)
    LP.given_opened()
    LP.login(email, password)

    LP.browser.element(".text-base.mb-5").should(have.text("Let's take a few minutes to setup your training "
                                                           "preferences. Getting these right will be important for "
                                                           "optimizing the way you train on Codewars."))


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка сайта Codewars')
@allure.story("Проверка открытия профиля")
@allure.link('https://www.codewars.com/', name='Testing')
def test_view_profile(setup_browser):
    email = newUser.email
    username = newUser.username
    password = newUser.password

    LP = CodeWarsPage(setup_browser)
    LP.given_opened()
    LP.login(email, password)

    LP.open_profile(username)

    LP.browser.matching(have.url("https://www.codewars.com/users/QATester123"))


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка сайта Codewars')
@allure.story("Проверка открытия настроек")
@allure.link('https://www.codewars.com/', name='Testing')
def test_account_settings(setup_browser):
    email = newUser.email
    password = newUser.password

    LP = CodeWarsPage(setup_browser)
    LP.given_opened()
    LP.login(email, password)

    LP.open_account_settings()

    LP.browser.matching(have.url("https://www.codewars.com/users/edit"))


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка сайта Codewars')
@allure.story("Проверка реддиректа на training setup")
@allure.link('https://www.codewars.com/', name='Testing')
def test_redirect_to_training_setup(setup_browser):
    email = newUser.email
    password = newUser.password

    LP = CodeWarsPage(setup_browser)
    LP.given_opened()
    LP.login(email, password)

    LP.browser.open("https://www.codewars.com/dashboard")
    LP.browser.matching(have.url("https://www.codewars.com/trainer/setup"))


@allure.tag('web')
@allure.label(Severity.BLOCKER)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка сайта Codewars')
@allure.story("Проверка открытия страницы практики")
@allure.link('https://www.codewars.com/', name='Testing')
def test_open_practice(setup_browser):
    email = newUser.email
    password = newUser.password

    LP = CodeWarsPage(setup_browser)
    LP.given_opened()
    LP.login(email, password)

    LP.open_practice()
    LP.browser.matching(have.url("https://www.codewars.com/kata/latest/my-languages?beta=false"))
