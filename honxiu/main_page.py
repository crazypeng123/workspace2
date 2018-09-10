from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time

browser = webdriver.Chrome()        #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
url = 'https://www.hongxiu.com/search'
t = 1                       #excel表格计数
for i in range(473, 964):
    browser.get(url)
    input = browser.find_element_by_id('s-box')  # 源码里输入框对应的标签内容
    input.clear()               #清空输入框
    input.send_keys(Input.articles[i])  # 输入框输入作品名
    input.send_keys(Keys.ENTER)
    if re.search('<h4><a href="[^>]*?"[\s\S]*?default">%s</a>'%Input.writers[i], browser.page_source):
        new_u = re.findall('字数</a>[\s\S]*<h4><a href="([^>]*?)"[\s\S]*?default">%s</a>' % Input.writers[i], browser.page_source)[0]
        new_url = ''.join(['https:', new_u])
        # time.sleep(10)
        browser.get(new_url)
        Soup = BeautifulSoup(browser.page_source, 'lxml')
        state = Soup.find('div', class_='book-info').find_all('i', 'blue')[0].get_text()                #状态
        contract = Soup.find('div', class_='book-info').find_all('i', 'blue')[1].get_text()             #是否签约
        label1 = Soup.find('div', class_='book-info').find_all('i')[-3].get_text()
        label2 = Soup.find('div', class_='book-info').find_all('i')[-4].get_text()                      #标签
        label = ','.join([label1, label2])
        word = Soup.find('div', class_='book-info').find_all('span')[-3].get_text()                    #字数
        words_u = Soup.find('div', class_='book-info').find_all('em')[3].get_text()                     #字数单位
        words = [word, words_u]
        collects = Soup.find('div', class_='book-info').find_all('span')[-2].get_text()                 #收藏数
        clicks = Soup.find('div', class_='book-info').find_all('span')[-1].get_text()                   #点击数
        week_ticket = Soup.find('div', class_='action-wrap').find('i', id='recCount').get_text()        #周票数
        month_ticket = Soup.find_all('div', class_='action-wrap')[1].find('i', id='monthCount').get_text() #月票数
        m = Soup.find('div', class_='right-wrap fr').find_all('p')[1].get_text()                        #作品数
        n = int(m)                                                                    #转换成数字,用于循环其他作品爬取
        anothers = []
        for j in range(n-1):
            another = Soup.find('div', class_='work-slides cf').find_all('h4')[j].find('a', target='_blank').get_text()
            anothers.append(another)                                                   #其他作品
            other_book = ','.join(anothers)
        ws.write(t, 0, Input.writers[i])
        ws.write(t, 1, Input.articles[i])
        ws.write(t, 2, browser.current_url)
        ws.write(t, 3, state)
        ws.write(t, 4, contract)
        ws.write(t, 5, label)
        ws.write(t, 6, words)
        ws.write(t, 7, collects)
        ws.write(t, 8, clicks)
        ws.write(t, 9, week_ticket)
        ws.write(t, 10, month_ticket)
        ws.write(t, 11, other_book)
        t =t + 1
        wb.save('honxiu_id.xls')
    else:
        continue

