from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from bs4 import BeautifulSoup
import re
import Input
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://127.0.0.1:1080')
browser = webdriver.Chrome(chrome_options=chromeOptions)

url = 'https://zh.wikipedia.org/wiki'
for i in range(468, 961):
    browser.get(url)
    input = browser.find_element_by_name('search')        # 源码里输入框对应的标签内容
    input.send_keys(Input.articles[i])                    # 输入框输入作品名
    input.send_keys(Keys.ENTER)
    Soup = BeautifulSoup(browser.page_source, 'lxml')
    try:
        if 'mw-search-results' in browser.page_source:
            content = Soup.find_all('div', class_='mw-search-results')[0].get_text().strip('\n')
            name = './维基百科_%s_%s.txt' % (Input.writers[i], Input.articles[i])
            f = open(name, "w+", encoding='utf-8')
            f.write(content)
        else:
            m = len(Soup.find_all('div', class_='mw-parser-output')) - 1
            content = Soup.find_all('div', class_='mw-parser-output')[m].get_text().strip('\n')
            name = './维基百科_%s_%s.txt' % (Input.writers[i], Input.articles[i])
            f = open(name, "w+", encoding='utf-8')
            f.write(content)
    except:
        continue