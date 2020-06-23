from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers import *

# driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.expedia.com")

driver.find_element(By.ID, "tab-flight-tab-hp").click()

time.sleep(3)

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("NYC")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("SFO")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("07/15/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("07/22/2020")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()

time.sleep(3)

driver.quit()







