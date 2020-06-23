from drivers import *

driver.get(url="http://newtours.demoaut.com")
driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

password = driver.find_element_by_name("password")
username = driver.find_element_by_name("userName")

username.send_keys("mercury")
password.send_keys("mercury")
driver.find_element_by_name("login").click()


