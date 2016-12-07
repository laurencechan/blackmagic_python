# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
search_box = driver.find_element_by_id("kw")
search_box.send_keys("Nesta")
search_box.submit()

if __name__ == '__main__':
    pass
