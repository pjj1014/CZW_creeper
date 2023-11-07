#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/4/27 15:26
# @Author  : 傑君
# @File    : testSelenium.py
# @Software: PyCharm
import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 1.创建1个浏览器
# driver = webdriver.Chrome()
#
# # 修改一些浏览器部分属性，绕过检测
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
#                        {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => false})"""})
#
# # 2.打开淘宝首页
# driver.get("https://search.bidcenter.com.cn/search?keywords={0}")

# 3.定位到搜索框
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="q"]').send_keys("巴黎世家丝袜")

# 4.定位搜索框 点击搜索
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button').click()

# 5.登录 帐号输入框
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/a[1]').click()
#
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="txtusername"]').send_keys('17623118604')
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="txtpassword"]').send_keys('pjj1314910')
#
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="login_login_btn"]').click()
# 滑块


# 关闭广告
# time.sleep(random.randint(2, 5))
# driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[1]/a/img').click()

# 输入 搜索
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH,'//*[@id="aliSearchInput"]').send_keys('档案')
# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH,'//*[@id="jq_btn_search"]').click()

driver = webdriver.Chrome()
# 修改一些浏览器部分属性，绕过检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => false})"""})

driver.get("https://search.bidcenter.com.cn/search?keywords={0}&page={1}".format("扫描", 2))


# time.sleep(random.randint(1, 3))
# iframe = driver.find_element(By.XPATH, '//*[@id="baxia-dialog-content"]')
# driver.switch_to.frame(iframe)  # 切换
# time.sleep(random.randint(1, 3))


# time.sleep(random.randint(1, 3))
# driver.find_element(By.XPATH, '//*[@id="nc_1_wrapper"]').click()
# button = driver.find_element(By.XPATH, '//*[@id="nc_1_wrapper"]')
# ActionChains(driver).drag_and_drop_by_offset(button,258, 0).perform()
# 2.打开淘宝首页

def nodeExists(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except:
        return False


list = []
for i in range(0, 21):

    driver.get("https://search.bidcenter.com.cn/search?keywords={0}&page={1}".format("图书馆", i))
    if nodeExists('//*[@id="nc_1_n1z"]'):
        button = driver.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')  # 找到滑块
        ActionChains(driver).drag_and_drop_by_offset(button, 258, 0).perform()  # 滑动到位置 258,0 坐标(x,y)
        driver.get("https://search.bidcenter.com.cn/search?keywords={0}&page={1}".format("图书馆", i))
    # #得到数据
    # time.sleep(1)
    divs = driver.find_elements(By.XPATH, '//div[@id="searchListArea"]/div[@class="ssjg-list_cell"]')

    for div in divs:
        dict = {}
        dict['标题'] = div.find_element(By.XPATH,
                                      './div[@class="ssjg-list_body fl"]/div[@class="ssjg-list_bt"]/a[@class="ssjg-title add_kwd_cookie"]').text
        dict['地区'] = div.find_element(By.XPATH,
                                      './div[@class="ssjg-list_body fl"]/div[@class="ssjg-list_foot"]/div[@class="fr"]/span[@class="diqu"]').text
        dict['链接'] = div.find_element(By.XPATH,
                                      './div[@class="ssjg-list_body fl"]/div[@class="ssjg-list_bt"]/a[@class="ssjg-title add_kwd_cookie"]').get_attribute(
            'href')
        list.append(dict)
print(list)
