# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Cookie": 'hasShowWeiyun675912623=1; lastshowtime675912623=1473385739856; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; randomSeed=956635; mobileUV=1_155c2d17be7_f252d; tvfe_boss_uuid=e79d6d2f96679c01; __Q_w_s__appDataSeed=1; eas_sid=e1b417b1T3y9x0h8b0h7i5q915; ptui_loginuin=1360508532; AMCV_248F210755B762187F000101%40AdobeOrg=793872103%7CMCIDTS%7C17055%7CMCMID%7C03653594988939970986104545897040821131%7CMCAAMLH-1474094965%7C11%7CMCAAMB-1474094965%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; pac_uid=1_675912623; o_cookie=675912623; pgv_pvid=6121923620; pgv_info=ssid=s9193246082; RK=vT0GKO4zMl; qzone_check=675912623_1475051520; pgv_pvi=3788326912; pgv_si=s7636697088; ptisp=cnc; ptcz=9e2f52219851303c1d1c7f248b0372ef982e2ac08f71db57dba1ee3da4c981ab; pt2gguin=o0675912623; uin=o0675912623; skey=@v8ng4ouCK; p_uin=o0675912623; p_skey=8JaQ9Wt-6CoXp9IYVMthlmK-pjvyO1SbasfCvne1YQc_; pt4_token=z4FFD6nALns0scJzYqNV5lVjKLBghnKCn7HHaY4hmLg_; Loading=Yes; qzspeedup=sdch; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=5',
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
# }
#
# driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
# driver.get("http://user.qzone.qq.com/675912623/2?t=0.8235386489547443")
# time.sleep(7)
#
# # print driver.page_source
# print driver.get_cookies()
# driver.get_screenshot_as_file("2.jpg")
# driver.close()
# print driver.find_element_by_id("content").text
# driver.close()
# assert "Python" in driver.title
#
# elem = driver.find_element_by_name('q')
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found" not in driver.page_source
# driver.close()
cookie = {
    "hasShowWeiyun675912623": 1, "lastshowtime675912623": 1473385739856, "__Q_w_s__QZN_TodoMsgCnt": 1,
    "__Q_w_s_hat_seed": 1, "randomSeed": 956635, "mobileUV": "1_155c2d17be7_f252d",
    "tvfe_boss_uuid": "e79d6d2f96679c01", "__Q_w_s__appDataSeed": 1, "eas_sid": "e1b417b1T3y9x0h8b0h7i5q915",
    "ptui_loginuin": 1360508532,
    "AMCV_248F210755B762187F000101%40AdobeOrg": "793872103%7CMCIDTS%7C17055%7CMCMID%7C03653594988939970986104545897040821131%7CMCAAMLH-1474094965%7C11%7CMCAAMB-1474094965%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE",
    "pac_uid": "1_675912623", "cpu_performance_v8": 4, "uid": 46486763, "pgv_pvid": 6121923620, "o_cookie": 675912623,
    "pt2gguin": "o0675912623", "uin": "o0675912623", "skey": "@buaWMnyJ1", "ptisp": "cnc", "RK": "vT0GKO4zMl",
    "qzone_check": "675912623_1475133140", "ptcz": "9e2f52219851303c1d1c7f248b0372ef982e2ac08f71db57dba1ee3da4c981ab",
    "p_skey": "JDhkGL0tiMlx7Jkv79CiXY4Nu-Z0fi-Q8AW25X8*x6E_", "p_uin": "o0675912623",
    "pt4_token": "M-At*Yedd5um4ULoODhE3zoqIHr9gQsZQ*m6QX1sH7M_", "qz_screen": "1920x1080",
    "pgv_info": "ssid:s5918323215", "QZ_FE_WEBP_SUPPORT": 1, "Loading": "Yes", "qzspeedup": "sdch"

}
driver = webdriver.Chrome()

# driver.set_window_position(20, 40)
# driver.set_window_size(1100, 700)

driver.get("http://qzone.qq.com/")
driver.add_cookie(cookie)
# driver.switch_to.frame('login_frame')

# driver.find_element_by_id("switcher_plogin").click()
# driver.find_element_by_id('u').clear()
# driver.find_element_by_id('u').send_keys('675912623')
# driver.find_element_by_id('p').clear()
# driver.find_element_by_id('p').send_keys('Rr64668688.')
# driver.find_element_by_id('login_button').click()

# driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
# driver.get("http://user.qzone.qq.com/675912623/2")
# time.sleep(7)

print driver.page_source

# print driver.get_cookies()

if __name__ == '__main__':
    pass
