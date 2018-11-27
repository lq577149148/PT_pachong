from appium import webdriver

import time

desired_caps = {

    'platformName':'Android',
    'platformVersion':'4.4.2',
    'deviceName':'127.0.0.1:52002',
    'appPackage':'com.taobao.thttps://music.163.com/aobao',
    'appActivity':'com.taobao.tao.welcome.Welcome',


}



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

driver.find_element_by_id("************").click()         # 点击元素

driver.find_element_by_xpath("************").click()      # 点击元素

driver.find_element_by_xpath("************").send_keys(u'123456')   # 发送键值

driver.quit()      # 退出 session
