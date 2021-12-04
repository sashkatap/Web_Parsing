import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''The script scroll down endless scroll site to the end and pars all quotes.
To start script print at console: python3 infinite_scroll.py

'''

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://quotes.toscrape.com/scroll')

# Wait max 30 sec until download the site. If yes-next step, no-stop script
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quotes')))

pause_time = 1  # 1 sec wait for the page to load, on a heavy site there will be more 

# defined the height of the page before scroll
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
# scroll down the page each 1 sec to the end    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
# compare heights and change "last_height"
    if new_height == last_height:
        break
    last_height = new_height    

# after scrolling to the end, find all quotes using its class="quote" on the page
quotes = driver.find_elements_by_class_name("quote")

# Check the number of quotes
print(len(quotes))


driver.quit()  # closed Chrome after executing the script - it's a good practise!