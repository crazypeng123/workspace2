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
    if 'lemmaWgt-secondsKnow-logo' in browser.page_source:          #是否有秒懂视频
        browser.find_element_by_xpath('//*[@id="lemmaWgt-secondsKnow"]/div/div/ul/li[1]/a/span[2]').click()
        browser.switch_to_window(browser.window_handles[-1])
        soup2 = BeautifulSoup(browser.page_source, 'lxml')
        if 'list-title' in browser.page_source:
            v_num = re.sub("\D", "", soup2.find('div', class_='dialog-list').find_all('span')[0].get_text()) #视频数
            for j in range(int(v_num)):
                xpath1 = '/html/body/dl/dd[2]/div/div[2]/ul/li[%d]/a/span[1]' % (j+1)
                browser.find_element_by_xpath(xpath1).click()
                soup3 = BeautifulSoup(browser.page_source, 'lxml')
                see = soup3.find('span', class_='bar-vv').get_text()
                ws.write(i + 1, 9+j, see)
                time.sleep(3)
                wb.save('baidu.xls')
        else:
            see = soup2.find('span',class_='bar-vv-num').get_text()
            ws.write(i + 1, 9, see)
            wb.save('baidu.xls')
    browser.find_element_by_xpath('/html/body/dl/dd[1]/em').click()
browser.quit()
