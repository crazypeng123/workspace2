from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
import re
import Input
import time

browser = webdriver.Chrome()        #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('collector')       #建立excel和sheet
url = 'https://book.douban.com/subject_search'
m = 1    #表格行数计数
try:
    for author in Input.authors:
        browser.get(url)
        time.sleep(2)
        input = browser.find_element_by_id('inp-query')     #源码里输入框对应的标签内容
        input.clear()                       #清空输入框
        input.send_keys(author)             #输入框输入作者名
        input.send_keys(Keys.ENTER)
        pre_number = re.findall(r'>([^>]*?)[^\d]*?人收藏', browser.page_source)
        # if len(pre_number) != 0:
        #     print(author, pre_number[0])
        # else:
        #     print(author, 0)
        url = browser.current_url           #更换为新的地址
        if len(pre_number) != 0:
            ws.write(m, 0, author)
            ws.write(m, 1, pre_number[0])   #判断是否为空，是就为0，否则打印收藏数
        else:
            ws.write(m, 0, author)
            ws.write(m, 1, 0)
        wb.save('collectorss.xlsx')         #存放在excel第一二列
        m = m+1
finally:
    browser.close()
