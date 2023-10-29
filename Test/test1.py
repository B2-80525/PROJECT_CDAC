# from selenium import webdriver
# import os

# path = "/home/sunbeam/Desktop/Project/Driver/chromedriver.exe"
#
# driver = webdriver.Chrome()
# driver.get(website)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
driver.get(website)

driver.quit()