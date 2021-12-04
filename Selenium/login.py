from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''The script do auto login on the site, which requires it.
In production, we take the login and password from the variable environment!
To start script print at console: python3 login.py

'''

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://quotes.toscrape.com/login')

# Wait max 30 sec until download the site. If yes-next step, no-stop script
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'username')))


# Find fields for login & password using xpath
login = driver.find_element_by_xpath("//input[@id='username']")
password = driver.find_element_by_xpath("//input[@id='password']")

# Login & password for the test studying site
login.send_keys('admin')
password.send_keys('admin')

# Find a login button and push it
login_btn = driver.find_element_by_xpath("//input[@value='Login']")
login_btn.click()


# Wait max 30 sec until download the first element of the site. If yes-next step, no-stop script
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quote')))

# Checking the result to receive html of the page at console
html = driver.page_source
print(html)


driver.quit()  # closed Chrome after executing the script - it's a good practise!