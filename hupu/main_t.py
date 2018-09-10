from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time
#帖子数
browser = webdriver.Chrome()        #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
url = 'https://my.hupu.com/search'
m=1
for i in range(964):
    time.sleep(1)
    browser.get(url)
    input = browser.find_element_by_id('J_inputSearch')  # 源码里输入框对应的标签内容
    input.clear()               #清空输入框
    input.send_keys(Input.writers[i], ' ', Input.articles[i])  # 输入框输入作品名
    input.send_keys(Keys.ENTER)
    Soup = BeautifulSoup(browser.page_source, 'lxml')
    if '条精确记录' in browser.page_source:
        s_num = re.findall("\D(\d+)条", browser.find_element_by_xpath('//*[@id="search_main"]/div[3]/h4').text)[0]
        # t_num = int(s_num)
        ws.write(m, 0, Input.writers[i])
        ws.write(m, 1, Input.articles[i])
        ws.write(m, 2, s_num)
        ws.write(m, 3, browser.current_url)
        m = m+1
        wb.save('步行街_num.xls')
    else:
        continue
