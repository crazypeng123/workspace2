from selenium import webdriver
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

for i in range(300, 790):
    print(Input_url.articles[i])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    try:
        url0 = '%sdiscussion/' % Input_url.url[i]
        page_source1 = xmlresolve(url0)
        soup1 = BeautifulSoup(page_source1, 'lxml')
        f_num = re.sub("\D", "", soup1.find_all('span', class_='count')[-1].get_text())
        num = int(f_num)
    except:
        continue
    m = 1
    ws.write(0, 0, '发帖人')
    ws.write(0, 1, '标题')
    ws.write(0, 2, '内容')
    for j in range(num//20 + 1):
        print(j)
        url1 = '%s?start=%d' % (url0, j*20)
        page_source2 = xmlresolve(url1)
        soup2 = BeautifulSoup(page_source2, 'lxml')
        c_num = len(soup2.find('table', id='posts-table').find_all('td', class_='time'))
        for k in range(c_num):
            href = soup2.find('table', id='posts-table').find_all('a')[2*k].get('href')
            page_source3 = xmlresolve(href)
            soup3 = BeautifulSoup(page_source3, 'lxml')
            user = soup3.find('span', class_='post-author-name').find('a').get_text()
            title = soup3.find('div', class_='book-content').find('h1').get_text()
            try:
                content = re.sub('\s', '', soup3.find('div', id='link-report').find('p').get_text())
            except:
                content = '/'
            ws.write(m, 0, user)
            ws.write(m, 1, title)
            ws.write(m, 2, content)
            m = m + 1
            name = '豆瓣论坛_%s_%s.xls' % (Input_url.writers[i], Input_url.articles[i])
            wb.save(name)
            time.sleep(1)
