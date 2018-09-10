from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input_url
import time
import random
import requests


def xmlresolve(url, cd=1):
    time.sleep(cd * random.uniform(0, 2))
    trycount = 1
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyUser = "HS3QK38WJ3LZA0ED"
    proxyPass = "3183407ED73042BB"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }
    proxy_handler = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    while trycount <= 4:
        try:
            response = requests.get(url, proxies=proxy_handler)
            # response = requests.get(url, headers=self.header_local, cookies = self.cookies,timeout=20)
            # headers = self.header
            # print(response.status_code)
            response.encoding = 'utf-8'  # 根据网页编码格式调整
            txt = response.text
            length = len(txt)
            if response.status_code == 200:
                # print 'Entered!====>:',url
                return txt  # txt
            else:
                print('length is too short:', length)
        except:
            print("can't open", url)
        trycount += 1
        time.sleep(trycount * 2)
    print("length not right")
    return 0

for i in range(179, 181):
    print(Input_url.articles[i])
    url0 = '%sreviews/' % Input_url.url[i]
    page_source = xmlresolve(url0)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    ws.write(0, 0, '评论人')
    ws.write(0, 1, '标题')
    ws.write(0, 2, '有用')
    ws.write(0, 3, '无用')
    ws.write(0, 4, '评论')
    soup1 = BeautifulSoup(page_source, 'lxml')
    book_num = re.sub("\D", "", soup1.find('title').get_text())
    num = int(book_num)
    m = 1
    for j in range(num//20 + 1):
        url1 = '%s?start=%d' % (url0, j*20)
        print(j)
        page_source1 = xmlresolve(url1)
        soup2 = BeautifulSoup(page_source1, 'lxml')
        c_num = len(soup2.find_all('div', class_='main review-item'))
        for k in range(c_num):
            href = soup2.find_all('div', class_='review-short')[k].get('data-rid')
            url2 = 'https://book.douban.com/review/%s/' % href
            page_source2 = xmlresolve(url2)
            soup3 = BeautifulSoup(page_source2, 'lxml')
            titles = soup3.find('div', class_='article').find('span').get_text()
            users = soup3.find('div', class_='review-content clearfix').get('data-author')
            useful = re.sub("\D", "", soup3.find('div', class_='main-panel-useful').find('button').get_text())
            useless = re.sub("\D", "", soup3.find('div', class_='main-panel-useful').find_all('button')[1].get_text())
            commment = re.sub('\s', '', soup3.find('div', class_='review-content clearfix').get_text())
            ws.write(m, 0, users)
            ws.write(m, 1, titles)
            ws.write(m, 2, useful)
            ws.write(m, 3, useless)
            ws.write(m, 4, commment)
            m = m + 1
            name = '豆瓣书评_%s_%s.xls' % (Input_url.writers[i], Input_url.articles[i])
            wb.save(name)


