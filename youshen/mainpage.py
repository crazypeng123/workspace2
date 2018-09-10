from selenium import webdriver
import xlwt
import re
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://127.0.0.1:1080')
browser = webdriver.Chrome(chrome_options=chromeOptions)
wb = xlwt.Workbook()
ws = wb.add_sheet('main')       #建立excel和sheet
ws.write(0, 0, '集数')
ws.write(0, 1, '观看数')
ws.write(0, 2, '赞')
ws.write(0, 3, '踩')
url = 'https://www.youtube.com/playlist?list=PLTJaWZoVPdT1MTeP5wohCkOpRaezh9kBK'
for i in range(1):
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="overlays"]/ytd-thumbnail-overlay-side-panel-renderer/yt-icon').click()
    time.sleep(2)
    m = 1
    for j in range(100):
        see = re.sub("\D", "", browser.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text)
        useful = browser.find_elements_by_xpath('//yt-formatted-string[@id="text"][@class="style-scope ytd-toggle-button-renderer style-text"]')[0].text
        useless = browser.find_elements_by_xpath('//yt-formatted-string[@id="text"][@class="style-scope ytd-toggle-button-renderer style-text"]')[1].text
        ws.write(m, 0, m+500)
        ws.write(m, 1, see)
        ws.write(m, 2, useful)
        ws.write(m, 3, useless)
        m = m + 1
        wb.save('youtube_锦绣未央1.xls')
        browser.find_element_by_xpath('//*[@id="movie_player"]/div[23]/div[2]/div[1]/a[2]').click()
        time.sleep(3)




