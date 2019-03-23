import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import fun.se as se

driver = webdriver.Chrome()
sleeping_time = 1
driver.get("https://www.amtrak.com/home")

from_keys = 'Washington, DC'
from_ID = 'WAS'
dest_keys = 'Boston, MA'
dest_ID = 'BOS'
#MM/DD/YY
depart_date = '03/28/2019'

se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div/input[2]', from_keys)

se.click_by_id(driver, from_ID)

se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/input[2]', dest_keys)

se.click_by_id(driver, dest_ID)

se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/input', depart_date)

se.click_by_id(driver, 'findtrains')


time.sleep(sleeping_time)
print("End!")
