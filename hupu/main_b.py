from selenium import webdriver
import xlwt
from bs4 import BeautifulSoup
import input_url
import time

browser = webdriver.Chrome()        #选择浏览器
m=1
wb = xlwt.Workbook()
ws = wb.add_sheet('comm')  # 建立excel和sheet
for i in range(140, 251):
    browser.get(input_url.url[i])
    time.sleep(1)
    url0 = browser.current_url
    for k in range(int(input_url.s_num[i])//20 + 1):
        url1 = '%s&page=%d' % (url0, k+1)
        browser.get(url1)
        Soup = BeautifulSoup(browser.page_source, 'lxml')
        b_num = len(Soup.find('table', class_='mytopic topiclisttr').find_all('td', class_='p_title'))
        for j in range(b_num):
            title = Soup.find('table', class_='mytopic topiclisttr').find_all('td', class_='p_title')[j].get_text()
            block = Soup.find('table', class_='mytopic topiclisttr').find_all('a', class_='blue')[j].get_text()
            urls = Soup.find('table', class_='mytopic topiclisttr').find_all('td', class_='p_title')[j].find('a').get('href')
            xpath1 = '//*[@id="search_main"]/div[3]/form/table/tbody[2]/tr[%d]/td[3]' % (j+1)
            xpath2 = '//*[@id="search_main"]/div[3]/form/table/tbody[2]/tr[%d]/td[4]' % (j+1)
            xpath3 = '//*[@id="search_main"]/div[3]/form/table/tbody[2]/tr[%d]/td[5]' % (j+1)
            xpath4 = '//*[@id="search_main"]/div[3]/form/table/tbody[2]/tr[%d]/td[6]' % (j+1)
            author = browser.find_element_by_xpath(xpath1).text
            times = browser.find_element_by_xpath(xpath2).text
            response = browser.find_element_by_xpath(xpath3).text
            brow_num = browser.find_element_by_xpath(xpath4).text
            ws.write(m, 0, input_url.articles[i])
            ws.write(m, 1, title)
            ws.write(m, 2, urls)
            ws.write(m, 3, block)
            ws.write(m, 4, author)
            ws.write(m, 5, times)
            ws.write(m, 6, response)
            ws.write(m, 7, brow_num)
            m = m+1
            wb.save('虎扑_url.xls')