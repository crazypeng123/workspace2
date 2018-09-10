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

url = 'https://www.google.com/'
wb = xlwt.Workbook()
ws = wb.add_sheet('comm')  # 建立excel和sheet
ws.write(0, 0, '作家')
ws.write(0, 1, '作品')
for i in range(961):
    try:
        ws.write(i+1, 0, Input.writers[i])
        ws.write(i+1, 1, Input.articles[i])
        browser.get(url)
        time.sleep(1)
        input = browser.find_element_by_id('lst-ib')      # 源码里输入框对应的标签内容
        input.send_keys(Input.writers[i])                    # 输入框输入作品名
        input.send_keys(Keys.ENTER)
        Soup = BeautifulSoup(browser.page_source, 'lxml')
        num2 = re.sub("\D", "", Soup.find('div', id='extabar').get_text())
        ws.write(i + 1, 2, num2)
        wb.save('google2.xls')
    except:
        continue