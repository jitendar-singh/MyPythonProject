from drivers import *

driver.get("https://cloud.redhat.com/openshift/")
print("url of first page is:{}".format(driver.title))

time.sleep(5)
driver.get("http://demo.automationtesting.in/Windows.html")
print("url of second page is:{}".format(driver.title))

time.sleep(5)
driver.back()
print("url of current page is:{}".format(driver.title))

time.sleep(5)
driver.forward()
print("url of current page is:{}".format(driver.title))





