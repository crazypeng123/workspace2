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
url = 'https://www.xxsy.net/search'
t = 1
for i in range(350, 1037):
    browser.get(url)
    time.sleep(1)
    input = browser.find_element_by_class_name('search-text')  # 源码里输入框对应的标签内容
    input.clear()               #清空输入框
    input.send_keys(Input.articles[i])  # 输入框输入作品名
    input.send_keys(Keys.ENTER)
    #print(browser.page_source)
    # print(re.findall('<h4>[\s\S]*?href="([^>]*?)"[\s\S]*?class="iconfont"></i>%s</a>'%Input.writers[i], browser.page_source))
    if re.search('<h4>[\s\S]*?href="([^>]*?)"[\s\S]*?class="iconfont"></i>%s</a>'%Input.writers[i], browser.page_source):
        pre_url = re.findall('<h4>[\s\S]*?href="([^>]*?)"[\s\S]*?class="iconfont"></i>%s</a>'%Input.writers[i], browser.page_source)
        new_url = 'http://www.xxsy.net%s'% pre_url[0]
        browser.get(new_url)
        Soup = BeautifulSoup(browser.page_source, 'lxml')
        w_num = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[1]/em').text    #字数
        complete = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[1]/span[2]').text   #是否完成
        category = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[1]/span[3]').text.split('：')[1]  #类别
        read_num = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[2]/em').text      #阅读人数
        cl_num = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[3]/em').text     #收藏人数
        sc_num = re.sub("\D", "",browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/div[4]/p/span').text)     #评分人数
        score = browser.find_element_by_xpath('//*[@id="curscore"]').text          #评分
        label = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/dl/dd/p[3]').text          #标签
        if '本书未加入VIP，不能投月票' != browser.find_element_by_xpath('//*[@id="fansinfo"]/div[2]/div/div[2]/div/dl/dd[1]/p').text:
            month_ticket = browser.find_element_by_css_selector('#fansinfo > div.column-piao > div > div.tab-bd > div > dl > dd:nth-child(1) > p.nums').text    #月票
        browser.find_element_by_xpath('//*[@id="fansinfo"]/div[2]/div/div[1]/span[2]').click()
        cm_ticket = browser.find_elements_by_css_selector('p.nums')[1].text    #评价票
        r_num = browser.find_element_by_xpath('//*[@id="bookfanscount"]').text    #打赏粉丝总数
        cm_num = re.sub("\D", "", browser.find_element_by_xpath('//*[@id="discuss_content"]/h3/span').text)   #全部评论数
        # print(cm_ticket)
        ws.write(t, 0, Input.writers[i])
        ws.write(t, 1, Input.articles[i])
        ws.write(t, 2, browser.current_url)
        ws.write(t, 3, w_num)
        ws.write(t, 4, complete)
        ws.write(t, 5, category)
        ws.write(t, 6, read_num)
        ws.write(t, 7, cl_num)
        ws.write(t, 8, sc_num)
        ws.write(t, 9, score)
        ws.write(t, 10, label)
        ws.write(t, 11, month_ticket)
        ws.write(t, 12, cm_ticket)
        ws.write(t, 13, r_num)
        ws.write(t, 14, cm_num)
        t = t + 1
        wb.save('潇湘_main.xls')