import xlrd

#导入作者名存在author集合里
file = xlrd.open_workbook('./source.xlsx')
writers = []        #作者名和文章一一对应
articles = []       #文章名
tables = file.sheets()
table = file.sheets()[0]
for i in range(table.nrows-2):
    writers.append(table.row_values(i+2)[0])
#print(authors)
#文章放在article里
for i in range(table.nrows-2):
    articles.append(table.row_values(i+2)[1])

# for i in range(len(writers)):
#     print(writers[i], articles[i])
