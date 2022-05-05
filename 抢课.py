#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
s = Service('D:\chromedriver.exe')
driver2 =  webdriver.Chrome(service=s)


# In[2]:


driver2.get("http://210.28.81.11/")


# In[3]:


verificationcode=input()
Username='21202*****' #学号
password='******'   #密码


# In[4]:


driver2.find_element(By.XPATH,'//*[@id="txtSecretCode"]').send_keys(verificationcode)


# In[5]:


driver2.find_element(By.XPATH,'//*[@id="txtUserName"]').send_keys(Username)


# In[6]:


driver2.find_element(By.XPATH,'//*[@id="TextBox2"]').send_keys(password)


# In[7]:


driver2.find_element(By.XPATH,'//*[@id="Button1"]').click()#登录按钮


# In[8]:


#driver.switch_to.frame


# In[9]:


move = driver2.find_element(By.XPATH,'//*[@id="navxl"]/li[2]/a/span')
ActionChains(driver2).move_to_element(move).perform()#悬浮鼠标，拉出选项卡


# In[10]:


driver2.find_element(By.XPATH,'//*[@id="navxl"]/li[2]/ul/li[1]/a').click() #通识选课


# In[11]:


driver2.switch_to.frame(driver2.find_element(By.XPATH,'//*[@id="iframeautoheight"]')) #进入iframe中,很重要，否则会找不到提交


# In[12]:


#driver2.find_element_by_xpath('//*[@id="dpkcmcGrid_btnLastPage"]').click()
#driver2.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页


# In[13]:


while True:
    element = driver2.find_element(By.XPATH,'//*[@id="kcmcGrid_xk_14"]')
    driver2.execute_script("arguments[0].click();", element)
    driver2.find_element(By.XPATH,'//*[@id="Button1"]').click()#提交
    alert = driver2.switch_to.alert
    driver2.switch_to.alert.accept()


# In[ ]:


#driver2.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页


# In[ ]:


#driver2.find_element_by_xpath('//*[@id="dpkcmcGrid_btnPrePage"]').click()#上一页






