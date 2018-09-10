from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://127.0.0.1:1080')
browser = webdriver.Chrome(chrome_options=chromeOptions)
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
m = 1
for i in range(961):
    url = 'https://www.youtube.com/channel/UC8KEjWaatGYJJ3WCCGeOEYw/search?query=%s' % Input.articles[i]
    browser.get(url)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    try:
        if Input.articles[i] in browser.find_element_by_xpath('//*[@id="dismissable"]/div').text:
            browser.find_element_by_xpath('//*[@id="dismissable"]/div').click()
            time.sleep(2)
            ws.write(m, 0, Input.writers[i])
            ws.write(m, 1, Input.articles[i])
            ws.write(m, 2, browser.current_url)
            wb.save('youshen_url.xls')
            m = m + 1
    except:
        continue
