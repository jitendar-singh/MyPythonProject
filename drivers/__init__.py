import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path=DRIVER_BIN)
