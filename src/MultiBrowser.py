from drivers import *

driver.get("https://cloud.redhat.com/openshift/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
driver.quit()
