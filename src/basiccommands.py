import time

from drivers import *

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
# print(driver.__doc__)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.quit()

