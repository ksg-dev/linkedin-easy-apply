from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()
LINK_EMAIL = os.environ["LINK_EMAIL"]
LINK_PW = os.environ["LINK_PW"]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3965477279&f_AL=true&geoId=103644278&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Click Sign In Button
time.sleep(2)
signin = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin.click()

# Key Elements - login
time.sleep(5)
email_txt = driver.find_element(By.ID, value="username")
email_txt.send_keys(LINK_EMAIL)

pw_txt = driver.find_element(By.ID, value="password")
pw_txt.send_keys(LINK_PW)
pw_txt.send_keys(Keys.ENTER)


# driver.quit()