# coding=utf-8

import cookielib, urllib2, requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": 'uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __message_district_code=230000; __utma=17226283.348199281.1466472479.1470205102.1474351237.3; __utmz=17226283.1474351237.3.2.utmcsr=write.blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/postlist; _ga=GA1.2.348199281.1466472479; _gat=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325,1474334971,1474429914,1474509612; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474509620; _message_m=zsyifkcfi3wbtrflpcrr1qyg; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474509624212; access-token=9202e56f-c23a-4632-a5c5-d7a1d0ad26c2; dc_tos=odvuyx; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; dc_session_id=1474509617183',
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

url = "http://write.blog.csdn.net/postlist"

# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# xx = opener.open(url)
# print xx.read()
# print type(xx)
# print cookie

# cookieFile = "Cookies_saved.txt"
# cookieJar = cookielib.MozillaCookieJar(cookieFile)
# cookieJar.save()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
#
# response_1 = urllib2.Request(url, headers=headers)
# response = opener.open(response_1)
# # print type(response)
# cookieJar.save()

# cookie = 'uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __message_district_code=230000; __utma=17226283.348199281.1466472479.1470205102.1474351237.3; __utmz=17226283.1474351237.3.2.utmcsr=write.blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/postlist; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474334971,1474429914,1474509612,1474512674; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474512679; _message_m=o40juaigebfb4amjfce4yh10; _ga=GA1.2.348199281.1466472479; _gat=1; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474512686062; access-token=76447bb2-5268-4ddf-9081-29e7d4716777; dc_tos=odvx9o; dc_session_id=1474512682050; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0'
#
# list_cookie = cookie.split(";")
# for i in list_cookie:
#     print i
# print cookie




if __name__ == '__main__':
    pass
