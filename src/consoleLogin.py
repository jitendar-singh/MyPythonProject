import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers import *
from selenium.webdriver.common.by import By

from agents import *

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
                                  "3]/input").send_keys("https://github.com/akram/scrum-planner.git")
    driver.find_element(By.ID, "yui-gen5-button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='yui-gen13-button']").click()


def buildjob():
    driver.find_element(By.XPATH, "//*[@id='tasks']/div[4]/a[2]").click()


def setnodejs12agentimages():
    # time.sleep(5)
    print("Manage Jenkins")
    driver.find_element(By.XPATH, "//*[@id='tasks']/div[4]/a[2]").click()

    '''
    Explicit wait for Configure Clouds option
    //*[@id="main-panel"]/div[13]/a/img
    '''
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-panel']/div[13]/a/img")))
    element.click()
    print("Clicked the cloud & Node configure button")

    '''
     Explicitly waiting for the configure clouds link.
     //*[@id="tasks"]/div[4]/a[2]
    '''
    waitconfigclouds = WebDriverWait(driver, 10)
    congifurecloud = waitconfigclouds.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tasks']/div[4]/a[2]")))
    congifurecloud.click()
    print("Clicked the configure cloud link")

    '''
         Explicitly waiting for the pod template button.
         //*[@id="yui-gen50-button"]
    '''

    waitbutton = WebDriverWait(driver, 20)
    try:
        button = waitbutton.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen50-button']")))
        button.click()
        print("Clicked the pod template button")
    except:
        print("Exception: Pod Templates button not ready")

    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
    #     )
    # finally:
    #     driver.quit()
    # "//*[@id='ui-gen45'/table/tbody/tr[1]/td[3]/input"

    # "//*[@id="yui-gen53-button"]"
    try:
        waitnodejs = WebDriverWait(driver, 10)
        nodejstemplate = waitnodejs.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen53-button']")))
        nodejstemplate.click()
        # driver.find_element(By.XPATH, ).click()
        print("Clicked pod button")
        podname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yui-gen45"
                                                                                            "']/table/tbody/tr[1]/td["
                                                                                            "3]/input")))
        driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[1]/td[3]/input").clear()
        driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[1]/td[3]/input").send_keys("nodejs12")
        print("Changed the pod name: " + nodejs12)
        print(podname)
    except:
        print("EXCEPTION: In pod name block")
    # time.sleep(3)

    try:
        podlabel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yui-gen45"
                                                                                             "']/table/tbody/tr["
                                                                                             "6]/td[3]/input")))
        driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[6]/td[3]/input").clear()
        driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[6]/td[3]/input").send_keys("nodejs12")
        print("Changed pod label: " + nodejs12)
        print(podlabel)
        print("Changing the docker image")
        driver.find_element(By.XPATH, "//*[@id='yui-gen27']/table/tbody/tr[5]/td[3]/input").clear()
        print("Changing the docker image")
        driver.find_element(By.XPATH, "//*[@id='yui-gen27']/table/tbody/tr[5]/td[3]/input").send_keys(nodejs12)
        print("Changed the docker image")
    except:
        print("EXCEPTION: In pod label section ")

    driver.find_element(By.XPATH, "//*[@id='yui-gen55']").click()
    print("Click on Apply")

    waitsave = WebDriverWait(driver, 10)
    elementsave = waitsave.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen72-button']")))
    elementsave.click()
    print("Click on Save")


if LOGIN_KEY in driver.title:
    loginfirsttry()
    jenkinsconsole()
    time.sleep(5)
    setnodejs12agentimages()
    createjob()
    pipelinejobsteps()
    buildjob()
else:
    logintryagain()
    jenkinsconsole()
    setnodejs12agentimages()
    createjob()
    pipelinejobsteps()
    buildjob()
