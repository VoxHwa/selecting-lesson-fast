<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8
# Author:VoxHwa

import ddddocr 
import selenium 
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
#from PIL import Image

options = Options()
options.add_argument('--window-size=1920,1080')   # 设置窗口界面大小
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Chrome(chrome_options=options)

def login(Username,password,driver=driver):
    driver.get("http://210.28.81.11/")
    time.sleep(1)
    icode=driver.find_element_by_id('icode')
    icode.screenshot("icode.png")
    #img=Image.open('icode.png')
    #img.show()
    ocr=ddddocr.DdddOcr()
    verificationcode=(ocr.classification(open('icode.png','rb').read()))
    
    driver.find_element_by_xpath('//*[@id="txtSecretCode"]').send_keys(verificationcode)

    driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(Username)

    driver.find_element_by_xpath('//*[@id="TextBox2"]').send_keys(password)

    driver.find_element_by_xpath('//*[@id="Button1"]').click()
    try:
        driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/a/span')
    except:
        login(Username,password)
        return 0

def mainpage(User,driver=driver):
    driver.get("http://210.28.81.11/xs_main.aspx?xh="+User)

    move = driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/a/span')
    ActionChains(driver).move_to_element(move).perform()#悬浮鼠标，拉出选项卡

    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[1]/a').click()#通识

    #driver.find_element_by_xpath('//*[@id="headDiv"]/ul/li[2]/ul/li[2]/a').click()#专业任意专限

    #driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[3]/a').click()#创新、外语

    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="iframeautoheight"]')) #进入iframe中,很重要，否则会找不到提交

    Select(driver.find_element_by_id('kj')).select_by_value('板块（1）')  



def alert_is_present(driver):
    try:
        alert = driver.switch_to.alert
        alert.text
        return alert
    except:
        return False


def loop(driver=driver):
    try:
        element = driver.find_element_by_xpath('//*[@id="kcmcGrid_xk_"]')
    except:
        time.sleep(1)
        mainpage(driver)
        loop(driver=driver)
        return 0
    driver.execute_script("arguments[0].click();", element)
    driver.find_element_by_xpath('//*[@id="Button1"]').click()#提交
    #alert = driver.switch_to.alert
    if alert_is_present(driver):
        driver.switch_to.alert.accept()


# main task
Username=''#学号
password=''#密码
login(Username,password)
while True:
    mainpage(Username)
    for i in range(1000):
        loop(driver)