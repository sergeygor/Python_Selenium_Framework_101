from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


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
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()













