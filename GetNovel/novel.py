from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import io
import time
diver = Chrome("F:/asir/asi/chromedriver.exe")
diver.get("http://www.shuquge.com/txt/108555/index.html")
mids = diver.find_elements_by_xpath("/html/body/div[5]/dl/dd")
book = diver.find_element_by_xpath("/html/body/div[4]/div[2]/h2")
x = len(mids)
m = str(book.text) + "totally have " + str(x) + "章"
print(m)
#获取封面 of 书
cover  = diver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/img")
link = cover.get_attribute("src")
filed = open("readme.html","w+")
filed.writelines('''<html>
<head>
    <title>
        我的师兄太稳健了.目录
    </title>
    
</head>
<body style="background-color: rgb(31, 27, 27);">
<p>
''')
filed.write(m + '\n')
filed.write('<img src="http://www.shuquge.com/files/article/image/108/108555/108555s.jpg" alt="我的师兄太稳健了">')
filed.write('''
    <p>

    </p>''')
for i in range(1,10):
    sc = "/html/body/div[5]/dl/dd"+'['+str(i)+']'
    mid = diver.find_element_by_xpath(sc)
    name = 'novels/' + mid.text + '.html'
    file = open(name,"w+")
    file.write('''
    <html>
<head>
    <title>
        我的师兄太稳健了.目录
    </title>
    
</head>
<body >
<p>
<pre>
    ''')
    filed.write('''
    <button>
    ''')
    filed.write('<a href = ' + "'" +name + "'>"+ name + '</a>' +'\n')
    filed.write('''
    </button>
    <p>

    </p>
    ''')
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,sc,)))
    ActionChains(diver).click(mid).perform()
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div[2]")))
    txts = diver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]")
    
    print(str(i) + 'th is downloading      （￣︶￣）↗' +'\n')
    
    file.write(txts.text + '\n'+'</p></body></html>')
    file.close()
    
    print(i,end ="th ")
    print('is successed download ヾ(✿ﾟ▽ﾟ)ノ ')
    
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/div/a[2]")))    
    back = diver.find_element_by_xpath("/html/body/div[4]/div[1]/div/a[2]")

    ActionChains(diver).click(back).perform()

print('That is all thank you for using me []~(￣▽￣)~*')
filed.write(str(mid))
filed.writelines('''

</p>
</body>
</html>
''')
diver.close()
