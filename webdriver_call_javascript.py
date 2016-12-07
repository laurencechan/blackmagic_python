# coding=utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.set_window_size(600,600)

driver.find_element_by_id("kw").send_keys("selenium")
sleep(3)
driver.find_element_by_class_name("bg s_btn").click()


js = "window.scrollTo(900,2000);"
driver.execute_script(js)
sleep(3)


if __name__ == '__main__':
    pass