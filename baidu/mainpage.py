from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time

browser = webdriver.Chrome()       #选择浏览器
wb = xlwt.Workbook()
ws = wb.add_sheet('comm')  # 建立excel和sheet
ws.write(0, 0, '作家')
ws.write(0, 1, '作品')
ws.write(0, 2, '百科地址')
ws.write(0, 3, '点赞数')
ws.write(0, 4, '浏览次数')
ws.write(0, 5, '文章数')
ws.write(0, 6, '阅读量')
ws.write(0, 7, 'TA说链接')
ws.write(0, 8, '单篇TA说链接')
ws.write(0, 9, '秒懂视频观看数1')
ws.write(0, 10, '浏览次数观看数2')
for i in range(961):
    ws.write(i + 1, 0, Input.writers[i])
    ws.write(i + 1, 1, Input.articles[i])
    url = 'https://baike.baidu.com/item/%s' % (Input.articles[i])
    browser.get(url)
    time.sleep(1)
    soup0 = BeautifulSoup(browser.page_source, 'lxml')
    ws.write(i + 1, 2, browser.current_url)
    try:
        use0 = soup0.find('span', class_='vote-count').get_text()           #点赞数
    except:
        use0 = soup0.find('i', class_='vote-count').get_text()
    brow = browser.find_element_by_xpath('//*[@id="j-lemmaStatistics-pv"]').text
    ws.write(i + 1, 3, use0)
    ws.write(i + 1, 4, brow)

    if 'tashuo-right' not in browser.page_source:
        ws.write(i + 1, 5, '无')
    if 'tashuo-more' not in browser.page_source:          #只有一条TA说
        ws.write(i + 1, 5, 1)
        browser.find_element_by_xpath('//*[@id="tashuo_right"]/div/div/div[2]/div/ul/li/div/div[2]/a/img').click()
        browser.switch_to_window(browser.window_handles[-1])
        ws.write(i + 1, 8, browser.current_url)
        soup1 = BeautifulSoup(browser.page_source, 'lxml')
        read = soup1.find('span', class_='read-item').find('strong').get_text()
        ws.write(i + 1, 6, read)
        time.sleep(2)

    if 'tashuo-more' in browser.page_source:                                       #多条TA说
        browser.find_element_by_xpath('//*[@id="tashuo_right"]/div/div/div[1]/a/span').click()
        browser.switch_to_window(browser.window_handles[-1])
        ws.write(i + 1, 7, browser.current_url)
        soup1 = BeautifulSoup(browser.page_source, 'lxml')
        banner = soup1.find('div', class_='banner-information').get_text()
        a_num = re.findall('文章\s*([\s\S]*?)\s*阅读\s*([\s\S]*)', banner)[0]
        print(a_num[0])
        ws.write(i + 1, 5, a_num[0])
        ws.write(i + 1, 6, a_num[1])
        wb.save('百度.xls')
        time.sleep(2)

browser.close()
