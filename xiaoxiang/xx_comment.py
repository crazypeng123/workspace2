from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import input_url

import time

browser = webdriver.Chrome()        #选择浏览器
m=1
for i in range(8,9):
    browser.get(input_url.url[i])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    time.sleep(1)
    Soup = BeautifulSoup(browser.page_source, 'lxml')
    cm_num = cm_num = re.sub("\D", "", browser.find_element_by_xpath('//*[@id="discuss_content"]/h3/span').text)
    num0 = int(cm_num)

    user0 = browser.find_element_by_xpath('//*[@id="total"]/div[2]/dl/dt/span[1]').text
    denf0 = browser.find_element_by_xpath('//*[@id="total"]/div[2]/dl/dt/span[2]').text
    comment0 = browser.find_element_by_xpath('//*[@id="total"]/div[2]/dl/dd').text
    ws.write(1, 0, user0)
    ws.write(1, 1, denf0)
    ws.write(1, 2, comment0)
    for j in range(num0//10):
        browser.find_element_by_xpath('//*[@id="reviewGetMore1"]').click()
        time.sleep(2)
    for k in range(0, num0-1):
        xpath1 = '//*[@id="reviewContent1"]/li[%d]/div[2]/dl/dt/span[1]'%(k+2)
        xpath2 = '//*[@id="reviewContent1"]/li[%d]/div[2]/dl/dt/span[2]'%(k+2)
        xpath3 = '//*[@id="reviewContent1"]/li[%d]/div[2]/dl/dd'%(k+2)
        user = browser.find_element_by_xpath(xpath1).text
        denf = browser.find_element_by_xpath(xpath2).text
        comment = browser.find_element_by_xpath(xpath3).text
        ws.write(k+2, 0, user)
        ws.write(k+2, 1, denf)
        ws.write(k+2, 2, comment)
        name = '潇湘书馆_%s_%s.xls' % (input_url.writers[i], input_url.articles[i])
        wb.save(name)
    browser.close()