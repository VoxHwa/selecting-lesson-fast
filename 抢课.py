#!/usr/bin/env python
# coding: utf-8

import selenium 
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://210.28.81.11/")

verificationcode=input()
Username=''
#教务系统账户
password=''
#教务系统密码

driver.find_element_by_xpath('//*[@id="txtSecretCode"]').send_keys(verificationcode)


driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(Username)


driver.find_element_by_xpath('//*[@id="TextBox2"]').send_keys(password)


driver.find_element_by_xpath('//*[@id="Button1"]').click()#登录按钮


#driver.find_element_by_xpath('//*[@id="headDiv"]/ul/li[2]/a/span').click()


#driver.switch_to.frame
time.sleep(1)
move = driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/a/span')
ActionChains(driver).move_to_element(move).perform()#悬浮鼠标，拉出选项卡


driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[1]/a').click()#通识


    #driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[2]/a').click()#专业任意专限


    #driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[3]/a').click()#创新、外语


driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="iframeautoheight"]')) #进入iframe中,很重要，否则会找不到提交



    #import warnings


    #warnings.filterwarnings("ignore")


def alert_is_present(driver):
    try:
        alert = driver.switch_to.alert
        alert.text
        return alert
    except:
        return False



#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页
#driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl3_xk"]').click()
#element = driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl3_xk"]')
#driver.execute_script("arguments[0].click();", element)


while True:
    try:
        element = driver.find_element_by_xpath('//*[@id="kcmcGrid_xk_4"]')
    except:
        pass
        driver.back()
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="kcmcGrid_xk_4"]')
    driver.execute_script("arguments[0].click();", element)
    driver.find_element_by_xpath('//*[@id="Button1"]').click()#提交
    #alert = driver.switch_to.alert
    if alert_is_present(driver):
        driver.switch_to.alert.accept()


alert = driver.switch_to.alert
driver.switch_to.alert.accept()


get_ipython().run_cell_magic('time', '', 'driver.find_element_by_xpath(\'//*[@id="kcmcGrid__ctl8_xk"]\').click()\ndriver.find_element_by_xpath(\'//*[@id="Button1"]\').click()#提交  \nalert = driver.switch_to.alert\ndriver.switch_to.alert.accept()')


#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页


#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnPrePage"]').click()#上一页


#driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl2_xk"]').click()


#driver.find_element_by_xpath('//*[@id="Button1"]').click()#提交

#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页

driver.switch_to.default_content()#返回主页面框架

#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

ActionChains(driver).send_keys(Keys.ENTER).perform()#回车键
