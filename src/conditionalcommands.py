from drivers import *

driver.get(url="http://newtours.demoaut.com")
# driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[1]")
password = driver.find_element_by_name("password")
username = driver.find_element_by_name("userName")

print(password.is_displayed())
print(password.is_enabled())

print(username.is_enabled())
print(username.is_displayed())

username.send_keys("mercury")
password.send_keys("mercury")
driver.find_element_by_name("login").click()

tripType = driver.find_element_by_css_selector("input[value=roundtrip]")
oneWay = driver.find_element_by_css_selector("input[value=oneway]")

print(tripType.is_selected())
print(oneWay.is_selected())
# driver.close()
