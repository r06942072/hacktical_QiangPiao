import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

    
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
sleeping_time = 1

browser.get("https://www.amtrak.com/home")
time.sleep(sleeping_time)
#search_bar = browser.find_element_by_class_name('search')
#search_bar = browser.find_element_by_id('tStation')
obj_from = browser.find_element_by_xpath('//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div/input[2]')
obj_from.send_keys('Washington, DC')

#obj_s = browser.find_element_by_class('search-station-dropdown__stations')
obj_from_2 = browser.find_element_by_id('WAS')
obj_from_2.click()
time.sleep(sleeping_time)

obj_to = browser.find_element_by_xpath('//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/input[2]')
obj_to.send_keys('Boston, MA')
time.sleep(sleeping_time)

obj_to_2 = browser.find_element_by_id('BOS')
obj_to_2.click()
time.sleep(sleeping_time)

obj_calendar = browser.find_element_by_xpath('//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/input')
obj_calendar.send_keys('03/28/2019')
time.sleep(sleeping_time)

obj_submit = browser.find_element_by_id('findtrains')
obj_submit.click()
time.sleep(sleeping_time)

print("End!")

