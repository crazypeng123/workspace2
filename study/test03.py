import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
url = 'http://www.xxsy.net/info/244402.html'
browser.get(url)
time.sleep(1)
Soup = BeautifulSoup(browser.page_source, 'lxml')
browser.find_element_by_xpath('//*[@id="fansinfo"]/div[2]/div/div[1]/span[2]').click()
cm_ticket = browser.find_elements_by_css_selector('p.nums')[1].text
print(cm_ticket)