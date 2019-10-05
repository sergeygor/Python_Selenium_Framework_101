from selenium import webdriver
import time

driver = webdriver.Chrome('../drivers/chromedriver')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

driver.find_element_by_id('welcome').click()
driver.find_element_by_link_text('Logout').click()

time.sleep(2)
driver.close()
driver.quit()