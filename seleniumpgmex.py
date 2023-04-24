from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://dev-reader.tcdcloud.com/jupiter/index.html")
print(driver.title)
# driver.find_element(By.XPATH, "//input[@id='session_key']").send_keys("nithyalakshmi.n@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys("afjadhfjdfh")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# driver.find_element(By.CLASS_NAME,"//*[contains(text(),'Password must be 8 characters or more.')]");
# print("Password must be 8 characters or more alret message is displayed")
print(driver.current_url)
driver.close()

# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()