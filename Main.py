import re

import threadpool

import dbtool

import requests
import time

import pictool

url = "http://jwzx.cqupt.edu.cn/jwzxtmp/pubBjsearch.php?action=bjStu"

username='yourUsername'
password='yourPassword'
database='yourDatabaseName'
db =dbtool.connection(username,password,database)


time1 = time.time()



text=requests.get(url).text
match = re.compile("target=_blank>(.*?)\(\\d+人\)</a>")
list = match.findall(text)
count = 0
pool=threadpool.ThreadPool(30)
for clazz in list:
    text=requests.get('http://jwzx.cqupt.edu.cn/jwzxtmp/showBjStu.php?bj=' + clazz).text
    content = re.compile("<tr>(.*?)</tr>").findall(text)
    for str in content:
        students = re.compile("<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>.*?src='(.*?)'").findall(str)
        for student in students:
            db.insert(student[1:])
            pictool.upload(student[1])

db.close()
time2 = time.time()
print(count)
print(time2-time1)

