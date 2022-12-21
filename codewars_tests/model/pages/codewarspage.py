import selene
from codewars_tests.model.controls.profiletopbarmenu import ProfileTopBarMenu
import allure


class CodeWarsPage:
    def __init__(self, browser: selene.Browser):
        self.browser = browser
        self.profile_top_bar_menu = ProfileTopBarMenu(self.browser.element("//li[@class='profile-item min-w-60px "
                                                                           "sm:min-w-130px has-menu mr-0 text-sm']"))

    def given_opened(self):
        self.browser.open("https://www.codewars.com/")
        return self

    @allure.step("Залогинится")
    def login(self, login, password):
        self.browser.element("//*[@id='login-btn']").click()

        self.browser.element("//*[@id='user_email']").send_keys(login)
        self.browser.element("//*[@id='user_password']").send_keys(password)
        self.browser.element("//button[contains(@class,'btn mt-3')]").click()

    @allure.step("Открыть профиль")
    def open_profile(self, username):
        self.profile_top_bar_menu.hover()

        self.browser.element(f"//a[@href='/users/{username}'][text()='View Profile']").click()

    @allure.step("Открыть настройки профиля")
    def open_account_settings(self):
        self.profile_top_bar_menu.hover()

        self.browser.element(f"//a[@href='/users/edit'][text()='Account Settings']").click()

    @allure.step("Открыть настройки профиля")
    def open_practice(self):
        self.browser.element("//*[@class='ml-1.5 w-6 h-6 inline-block']").hover()

        self.browser.element(f"//*[@href='/kata/latest/my-languages?beta=false']").click()
