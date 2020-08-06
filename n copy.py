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
big = diver.find_element_by_xpath("/html/body/div[5]/dl")
book = diver.find_element_by_xpath("/html/body/div[4]/div[2]/h2")
x = len(mids)
m = str(book.text) + "totally have " + str(x) + "章"
for mid in mids:
    name = 'x/' + mid.text + '.txt'
    file = open(name,'w+')
    ActionChains(diver).click(mid).perform()
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div[2]")))
    txts = diver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]")
    file.write(txts.text + '\n')
    print('is successed download ヾ(✿ﾟ▽ﾟ)ノ ')
    file.close()
    WebDriverWait(diver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/div/a[2]")))    
    back = diver.find_element_by_xpath("/html/body/div[4]/div[1]/div/a[2]")
    ActionChains(diver).click(back).perform()


