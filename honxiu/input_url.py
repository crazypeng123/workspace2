import xlrd
import re

#导入作者名存在author集合里
file = xlrd.open_workbook('./url.xls')
writers = []        #作者名和文章一一对应
articles = []       #文章名
url = []
url_id = []
tables = file.sheets()
table = file.sheets()[0]
for i in range(table.nrows-1):
    writers.append(table.row_values(i+1)[0])

for i in range(table.nrows-1):
    articles.append(table.row_values(i+1)[1])
for i in range(table.nrows-1):
    url.append(table.row_values(i+1)[2])
    # url_id.append(re)
# print(writers[6], articles[6], url[6])
