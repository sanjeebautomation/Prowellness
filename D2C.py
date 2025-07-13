import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
def test_Navigateurl():
    driver.get("https://prowellnessclub.dev.vasquezplatform.com/DirectMemberEnrollment")
    driver.maximize_window()
    time.sleep(5)
test_Navigateurl()
def test_Userinformation():
    driver.find_element(By.XPATH,'//input[@placeholder="First Name"]').send_keys("Sanjeeb")
    driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Nayak")
    driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("sanjeeb.nayak123@yopmail.com")
    driver.find_element(By.XPATH,"//input[@id='phone-number']").send_keys("7412589630")
    driver.find_element(By.XPATH,"//input[@id='icon']").send_keys("05/16/1990")
    driver.find_element(By.XPATH,"//input[@value='Male']").click()
    driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("Bhubaneswar")
    driver.find_element(By.XPATH,"//input[@id='city']").send_keys("Bhubaneswar")
    driver.find_element(By.XPATH,'//select[@id="state"]').click()
    driver.find_element(By.XPATH,'//option[@value="Alabama"]').click()
    driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("12345")
    time.sleep(5)
test_Userinformation()
def test_Getpricing():
    driver.find_element(By.XPATH, "//button[normalize-space()='Get Pricing']").click()
    driver.find_element(By.XPATH,'//tbody/tr[2]/td[1]/input[1]').click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Next']").click()
    time.sleep(5)
test_Getpricing()