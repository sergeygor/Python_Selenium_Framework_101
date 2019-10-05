from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="session")
def test_setup():
    global driver
    driver = webdriver.Chrome('/Users/sergeygordeev/Desktop/EDU/Python/Python_Selenium_Framework_101/drivers/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    time.sleep(2)
    driver.close()
    driver.quit()


def test_login(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()

def test_logout(test_setup):
    driver.find_element_by_id('welcome').click()
    driver.find_element_by_link_text('Logout').click()












