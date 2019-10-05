from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils as utils


class TestLogin:
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome('/Users/sergeygordeev/Desktop/EDU/Python/Python_Selenium_Framework_101/drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        time.sleep(2)
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()













