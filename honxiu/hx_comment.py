from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import input_url
import time

browser = webdriver.Chrome()  # 选择浏览器
m = 0
for i in range(46, 47):
    browser.get(input_url.url[i])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    time.sleep(1)
    Soup = BeautifulSoup(browser.page_source, 'lxml')
    if 'data-pagemax' in browser.page_source:
        page = Soup.find('div', class_='pagination')['data-pagemax']
        page1 = int(page)
        # print(input_url.articles[i], page)
        if page == 0:
            continue
        else:
            m = 0
            ws.write(0, 0, '评论人')
            ws.write(0, 1, '评论时间')
            ws.write(0, 2, '评论')
            for j in range(page1):
                text0 = browser.page_source.split(r'<div class="comment-list"')[-1]
                # text0 = re.findall(r'id="userCommentWrap">([\s\S]*?)<div class="page-box', text)     #取出评论区
                comment = re.findall('target="_blank">([^<]*?)</a>\s', text0)  # 评论
                user = re.findall('user-name default">([\s\S]*?)</a><i>', text0)  # 评论人
                pre_time = re.findall('</i><em>([\s\S]*?)</em>', text0)  # 原始时间
                real_time = []  # 完整时间
                for k in pre_time:
                    t = re.sub(r'今天', time.strftime('%m-%d') + ' ', k)
                    real_time.append(t)
                for l in range(len(user)):
                    m = m + 1
                    ws.write(m, 0, user[l])
                    ws.write(m, 1, real_time[l])
                    ws.write(m, 2, comment[l])
                if page1 < 7:
                    xpath = '//*[@id="page-container"]/div/ul/li[%d]/a' % (page1 + 2)
                else:
                    xpath = '//*[@id="page-container"]/div/ul/li[9]/a'
                browser.find_element_by_xpath(xpath).click()
                time.sleep(1)
                name = '红袖添香_%s_%s.xls' % (input_url.writers[i], input_url.articles[i])
                wb.save(name)
    else:
        continue
