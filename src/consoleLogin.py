import random

from drivers import *
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


LOGIN_KEY = "oauth-openshift"
driver.maximize_window()
driver.get("http://jenkins-jenkins-test.apps.jenkins-dev-4.5-062304.qe.devcluster.openshift.com")

driver.find_element(By.ID, "details-button").click()
driver.find_element(By.ID, "proceed-link").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/a").click()


def loginfirsttry():
    print("Inside first try")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/ul/li[1]/a").click()
    driver.find_element(By.ID, "inputUsername").send_keys("kubeadmin")
    driver.find_element(By.ID, "inputPassword").send_keys("MjTzN-aIo4K-QskYG-xTeay")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[4]/button").click()


def logintryagain():
    print("Inside logintryagain")
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()
    # driver.find_element(By.XPATH, "/html/body/div/div[2]/a").click()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/ul/li[1]/a").click()
    driver.find_element(By.ID, "inputUsername").send_keys("kubeadmin")
    driver.find_element(By.ID, "inputPassword").send_keys("MjTzN-aIo4K-QskYG-xTeay")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[4]/button").click()


def jenkinsconsole():
    print("Inside Jenkins console")
    try:
        driver.find_element(By.XPATH, "/html/body/form/div[2]/input[1]").click()
    except:
        print("EXCEPTION: No such element ")


def jenkinslogout():
    print("Logging you out")
    driver.find_element(By.XPATH, "//*[@id='header']/div[3]/a[2]/span").click()


def createjob():
    jobnum = random.randint(3, 99)
    jobname = "sample pipeline" + "-" + str(jobnum)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//*[@id='tasks']/div[1]/a[2]").click()
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys(jobname)
    driver.find_element(By.XPATH, "//*[@id='j-add-item-type-standalone-projects']/ul/li[2]/label/span").click()
    time.sleep(5)
    driver.find_element(By.ID, "ok-button").click()


def pipelinejobsteps():
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[2]/td[3]/textarea").send_keys(
        "Sample pipeline build to test nodejs agent & maven agent")
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[148]/td[3]/select").click()
    driver.find_element(By.XPATH,
                        "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[148]/td[3]/select/option[2]").click()
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                  "12]/td[3]/select").click()
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                  "12]/td[3]/select/option[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                  "13]/td[2]/table/tbody/tr[5]/td[3]/div/div[1]/table/tbody/tr[1]/td["
                                  "3]/input").send_keys("https://github.com/akram/pipes.git")
    driver.find_element(By.ID, "yui-gen5-button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='yui-gen13-button']").click()


def buildjob():
    driver.find_element(By.XPATH, "//*[@id='tasks']/div[4]/a[2]").click()


if LOGIN_KEY in driver.title:
    loginfirsttry()
    jenkinsconsole()
    # jenkinslogout()
    createjob()
    pipelinejobsteps()
    buildjob()
else:
    logintryagain()
    jenkinsconsole()
    # jenkinslogout()
    createjob()
    pipelinejobsteps()
    buildjob()
