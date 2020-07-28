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
filed = open("x/readme.txt","w+")
filed.write(m + '\n')
filed.write( '封面为' + str(link))
for i in range(1,100):
    sc = "/html/body/div[5]/dl/dd"+'['+str(i)+']'
    mid = diver.find_element_by_xpath(sc)
    name = 'x/' + mid.text + '.txt'
    file = open(name,"w+")
    filed.write(mid.text + '\n')
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,sc,)))
    ActionChains(diver).click(mid).perform()
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div[2]")))
    txts = diver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]")
    print(str(i) + 'th is downloading      （￣︶￣）↗' +'\n')
    file.write(txts.text + '\n')
    print(i,end ="th ")
    print('is successed download ヾ(✿ﾟ▽ﾟ)ノ ')
    file.close()
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/div/a[2]")))    
    back = diver.find_element_by_xpath("/html/body/div[4]/div[1]/div/a[2]")
    ActionChains(diver).click(back).perform()
print('That is all thank you for using me []~(￣▽￣)~*')
diver.close()
