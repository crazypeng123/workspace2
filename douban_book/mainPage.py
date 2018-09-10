from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time
import random

browser = webdriver.Chrome()        #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
url = 'https://book.douban.com/subject_search'
m = 0
for i in range(391, 400):
    m=m+1
    print(i)
    browser.get(url)
    x = random.uniform(3, 5)
    time.sleep(x)
    input = browser.find_element_by_id('inp-query')     #源码里输入框对应的标签内容
    input.clear()               #清空输入框
    input.send_keys(Input.articles[i], ' ', Input.writers[i])  # 输入框输入作者名和作品名
    input.send_keys(Keys.ENTER)
    y = random.uniform(3, 5)
    time.sleep(y)
    ws.write(m, 0, Input.writers[i])
    ws.write(m, 1, Input.articles[i])                   #打印作者和书名
    if browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div[2]'):
        continue
    else:
        xpath_urls = '//div[@class="item-root"]/a'
        urls_pre = browser.find_elements_by_xpath(xpath_urls)
        new_url = urls_pre[0].get_attribute("href")        #从搜索页面选第一个结果，找到链接打开作品主页
        browser.get(new_url)
        ws.write(m, 2, browser.current_url)
        Soup = BeautifulSoup(browser.page_source, 'lxml')
        publish = re.findall('出版社:</span>([\s\S]*?)<br', browser.page_source)
        if not publish:
            publish = 'null'
        else:
            ws.write(m, 3, publish[0])
        subtitle = re.findall('副标题:</span>([\s\S]*?)<br', browser.page_source)
        if not subtitle:
            subtitle = 'null'
        else:
            ws.write(m, 4, subtitle[0])
        years = re.findall('出版年:</span>([\s\S]*?)<br', browser.page_source)
        if not years:
            years = 'null'
        else:
            ws.write(m, 5, years[0])
        page = re.findall('页数:</span>([\s\S]*?)<br', browser.page_source)
        if not page:
            page = 'null'
        else:
            ws.write(m, 6, page[0])
        price = re.findall('定价:</span>([\s\S]*?)<br', browser.page_source)
        if not price:
            price = 'null'
        else:
            ws.write(m, 7, price[0])
        bind = re.findall('装帧:</span>([\s\S]*?)<br', browser.page_source)
        if not bind:
            bind = 'null'
        else:
            ws.write(m, 8, bind[0])
        Series = re.findall('>丛书:</span>[\s\S]*?>([\s\S]*?)</a>', browser.page_source)
        if not Series:
            Series = 'null'
        else:
            ws.write(m, 9, Series[0])
        i_num = re.findall('ISBN:</span>([\s\S]*?)<br', browser.page_source)
        if not i_num:
            i_num = 'null'
        else:
            ws.write(m, 10, i_num[0])
        evaluate = Soup.find('div', class_='rating_self clearfix').find('strong').get_text()
        c_num = re.sub("\D", "", Soup.find('div', class_='rating_sum').find('span').get_text())
        ws.write(m, 11, evaluate)
        ws.write(m, 12, c_num)
        if '人评价' in browser.page_source:
            eva1 = Soup.find_all('span', class_='rating_per')[0].get_text()
            eva2 = Soup.find_all('span', class_='rating_per')[1].get_text()
            eva3 = Soup.find_all('span', class_='rating_per')[2].get_text()
            eva4 = Soup.find_all('span', class_='rating_per')[3].get_text()
            eva5 = Soup.find_all('span', class_='rating_per')[4].get_text()
            ws.write(m, 13, eva1)
            ws.write(m, 14, eva2)
            ws.write(m, 15, eva3)
            ws.write(m, 16, eva4)
            ws.write(m, 17, eva5)
            z = random.uniform(3, 5)
            time.sleep(z)
        else:
            z = random.uniform(3, 5)
            time.sleep(z)
        wb.save('豆瓣_主页面.xls')



