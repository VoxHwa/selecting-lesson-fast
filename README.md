# 南京财经大学 南财教务系统（NUFE 选课自动化辅助，基于selenium)  
## 特性
1. 无需输入验证码
2. 高频率尝试选课
## 使用方法  

__1.安装电脑浏览器的驱动driver（需要对应浏览器版本）__
  
  1. **Chrome driver**（代码以Chrome为例）
  
  <http://npm.taobao.org/mirrors/chromedriver/>
  或者
  <http://chromedriver.storage.googleapis.com/index.html>
  
  2. **Edge driver**（在“关于Microsoft Edge”中查看）
  
  <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>

  
__2. 安装到本地对应浏览器目录文件夹__


___

__2.需要有Python环境（安装Python）__
1. 可以参考<https://blog.csdn.net/weixin_49237144/article/details/122915089>
2. 进入cmd(windows命令提示符,Win+R键)输入"python"（**如果提示"Python不是内部或外部命令",去配置一下环境变量**）

我的电脑$\rightarrow$属性$\rightarrow$高级->环境变量$\rightarrow$系统变量中的PATH为:

**变量名：** PATH

**变量值：**;C:\Python35;C:\Python35\Scripts; （**分号隔开**）


___

__3.安装selenium的库__
1. 参考<https://blog.csdn.net/zhniy/article/details/128471681>
```python
pip install selenium
```
```python
pip install ddddocr#顺便安装这个库
```
___


__4.调整代码参数（账户、密码、选课的元素位置）__
1. 注释
```python
import ddddocr #自动输入验证码模块
```
2. 账户（**别删引号！**）
```python
# main task
Username='这里输入学号'
password='这里输入密码'
```
3. 选课的元素位置更改
```python
def loop(driver=driver):
    try:
        element = driver.find_element_by_xpath('//*[@id="kcmcGrid_xk_61"]')
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
```
找到：
```python
element = driver.find_element_by_xpath('//*[@id="kcmcGrid_xk_61"]')
```
==61是最重要的参数==
更改方式（以Edge为例）：
找到想抢的课$\rightarrow$鼠标右键选择框$\rightarrow$菜单中选择“检查”$\rightarrow$在控制台中找到对应的数值$\rightarrow$更改程序的参数



## Todo list
~~细化教程，服务大众~~
制作GUI（？）

___
## 资助

<img src="https://github.com/VoxHwa/selecting-lesson-fast/blob/main/payment/alipay.jpg" width = "200" height = "300" alt="" align=left />
<img src="https://github.com/VoxHwa/selecting-lesson-fast/blob/main/payment/wechat.jpg" width = "200" height = "300" alt="" align=right/>
