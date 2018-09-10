from selenium import webdriver
import xlwt
from bs4 import BeautifulSoup
import re
import input_url
import input_tiezi
import time

browser = webdriver.Chrome()        #选择浏览器
m = 4395
for i in range(220, 250):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('comm')  # 建立excel和sheet
    ws.write(0, 0, '名称')
    ws.write(0, 1, '内容')
    ws.write(0, 2, '一楼')
    ws.write(0, 3, '二楼')
    m = m + int(input_url.s_num[i])
    for j in range(m-int(input_url.s_num[i]), m):
        browser.get(input_tiezi.url[j])
        title = re.findall(r'class="quote-content">\s*([^<]*?)\s*<br', browser.page_source)
        ws.write(j + int(input_url.s_num[i]) - m+1, 0, input_tiezi.names[j])
        ws.write(j+int(input_url.s_num[i])-m+1, 1, title)
        n = 2
        page = min(int(input_tiezi.x_num[j])//20 + 1, 10)       #只取帖子前十页
        for k in range(page):
            a_id = re.sub("\D", "", input_tiezi.url[j])
            new_url = 'https://bbs.hupu.com/%s-%d.html' % (a_id, k+1)
            browser.get(new_url)
            time.sleep(2)
            Soup = BeautifulSoup(browser.page_source, 'lxml')
            b_num = len(Soup.find_all('div', class_='floor-show'))
            for l in range(b_num - 1):
                comment = Soup.find_all('div', class_='floor-show')[l+1].find_all('td')[0].get_text()
                ws.write(j+int(input_url.s_num[i])-m+1, n, comment)
                n = n+1
                name = '虎扑_%s_%s.xls' % (input_url.writers[i], input_url.articles[i])
                wb.save(name)
