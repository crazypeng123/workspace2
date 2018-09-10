import xlrd

#导入作者名存在author集合里
file = xlrd.open_workbook('./youshen_url.xls')
writers = []        #作者名和文章一一对应
articles = []       #文章名
url = []
tables = file.sheets()
table = file.sheets()[0]
for i in range(table.nrows-1):
    writers.append(table.row_values(i+1)[0])
#print(authors)
#文章放在article里
for i in range(table.nrows-1):
    articles.append(table.row_values(i+1)[1])

for i in range(table.nrows-1):
    url.append(table.row_values(i+1)[2])
print(url[5])