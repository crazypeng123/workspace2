from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import input_url
import time

browser = webdriver.Chrome()        #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
for i in range(3,4):
    browser.get(input_url.url[i])
    time.sleep(1)
    Soup = BeautifulSoup(browser.page_source, 'lxml')
    print(browser.page_source)
    if 'data-pagemax' in browser.page_source:
        page = Soup.find('div', class_='pagination')['data-pagemax']
        # print(input_url.articles[i], page)
        # if page == 0:
        #     continue
        # else:
        #

    else:
        continue

