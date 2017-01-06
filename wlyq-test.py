# coding:utf-8
import urllib
import urllib2
import re

user_agent = 'Mobile/12A4345d Safari/600.1.4'   
headers = {'User-Agent': 'user_agent'}
count = -1
for i in range(1,4):
    url = 'http://www.chaling.gov.cn/index.php?mod=part&pid=355&page='+str(i)
    req = urllib2.Request(url,headers = headers)
    webcode = urllib2.urlopen(req).read()
    pattern = re.compile(r'<li><a href=".*?</li>',re.S)
    wlyq = re.findall(pattern,webcode)
    for title in wlyq:
        context = re.sub('useover.*>.*','',title[46:-9])
        print context
        f = open('clyuqing'+'.txt','a') #  'a'是追加模式，可以显示所有行， ‘w’只有一行 见核心编程p213 文件内建函数, 对比测试'r', 'r+','w+', 'a+'..
#w新建只写，w+新建读写，二者都会将文件内容清零,以a,a+的方式打开文件，附加方式打开  见http://blog.csdn.net/ztf312/article/details/47259805
        #a+ 会出现乱码  ； 'a'也能创建文件，那么，a和w的区别在哪里呢，何况w会清零覆盖，对于for语句应该不好，为什么看到的例子都是'w'？
        f.write(context+'\n')
        f.close()
