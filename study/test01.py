name =['a1','a2','a3']
f = open("./name.txt", "w+")
for i in name:
    f.write(i)
name = './维基百科_%s_%s.txt' % (Input.writers[i], Input.articles[i])
f = open(name, "w+", encoding='utf-8')
f.write(content)