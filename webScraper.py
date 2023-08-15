#please check the dependencies.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time 
import numpy as np
import pandas as pd

driver = webdriver.Chrome()
#DO NOT delete this function, unexpected behaviour may happen
driver.maximize_window()

#IMPORTANT : Change the url to scrape new content in ICE2023
url = "https://codecombat.com/play/ladder/ace-of-coders"
driver.get(url)

#Action chain is used instead of simple click() method
#->This is because this web is broken
action = ActionChains(driver)

wait = WebDriverWait(driver,timeout=20)
#scrape dynamic page content using selenium
#using bs4 as html parser for simplicity
#parse the required data as dataframe and export to googleSheet

#accept cookie
cookie = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'cc-allow')))
cookie.click()
time.sleep(2)


#click until no more 'show more' 

#please modify MAX_ITR as you wish 

#1 click = 100 students , total student ~ 8000
MAX_ITR = 100
i=0
while(i<MAX_ITR):
    try:
        item = wait.until(EC.element_to_be_clickable((By.ID,'load-more')))
        action.move_to_element(item).click().perform()
        #DONT change the time, their web cannot handle so much request
        time.sleep(2)
        i+=1
    except Exception: 
        break

print("scraping done")

#!!IMPORTANT!!
#Please modify the XPath when required, it is very likely that the path has to be modified for the new web.
wait.until(EC.visibility_of_element_located((By.XPATH,'.//table[contains(@class,"ladder-table")]')))
tableHeader = [cell.text for cell in driver.find_elements(By.XPATH,'.//table/thead/tr[2]/th')]
data = [cell.text for cell in driver.find_elements(By.XPATH,'.//table[contains(@class,"ladder-table")]/tbody/tr/td') ]

#reshape 1d array -> 2d array -> pandas dataframe w/ header
data = np.array(data,dtype=str)
data = data.reshape(-1,9)
df = pd.DataFrame(data,columns=tableHeader)

#keep a record to isolate the process, web scraping is too time consuming
df.to_csv('data.csv')

driver.quit()