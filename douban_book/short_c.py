from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input_url
import time
import random
browser = webdriver.Chrome()        #选择浏览器
m=1
for i in range(353, 370):
    print(Input_url.articles[i])
    url0 = '%scomments/' % Input_url.url[i]             #拼接作品主网址
    browser.get(url0)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    ws.write(0, 0, '用户')
    ws.write(0, 1, '有用')
    ws.write(0, 2, '评论')
    x = random.uniform(60, 75)
    time.sleep(x)
    short_num = re.sub("\D", "", browser.find_element_by_xpath('//*[@id="total-comments"]').text)   #获取该作品短评数
    num = int(short_num)
    m = 1
    for j in range(num//20 + 1):
        print(j+1)
        url1 = '%shot?p=%d' % (url0, j+1)                   #拼接每页评论的网址
        p_num = 0
        while p_num == 0:
            browser.get(url1)
            y = random.uniform(13, 19)
            time.sleep(y)
            try:
                Soup = BeautifulSoup(browser.page_source, 'lxml')
                p_num = len(Soup.find('div', class_='comments-wrapper').find_all('p', class_='comment-content'))    #每页评论条数
                for k in range(p_num):
                    user = Soup.find('div', class_='comments-wrapper').find_all('span', class_='comment-info')[k].find('a').get_text()#用户
                    useful = Soup.find('div', class_='comments-wrapper').find_all('span', class_='vote-count')[k].get_text()  # 有用
                    comment = Soup.find('div', class_='comments-wrapper').find_all('p', class_='comment-content')[k].find('span', class_='short').get_text()                                              #评论
                    ws.write(m, 0, user)
                    ws.write(m, 1, useful)
                    ws.write(m, 2, comment)
                    m = m + 1
                    name = '豆瓣读书_%s_%s.xls' % (Input_url.writers[i], Input_url.articles[i])
                    wb.save(name)
            except:
                print('sleep')
                time.sleep(1200)
browser.close()

