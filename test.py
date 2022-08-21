# @Time: 2022/8/21 13:27
# @Author: DoubleApple
import time
import datetime
import requests

'''
ulr1  羽毛球可选日期页面
GET https://mapv2.51yundong.me/api/stadium/resources/2c93809e821eb0ed01822a128aaf00b8/dates?stadiumItemId=2c93809e821eb0ed01822a128aaf00b8 HTTP/1.1
Host: mapv2.51yundong.me
Connection: keep-alive
Authorization: Bearer 600f48d7-89b6-4a7f-a5d4-ada10b2e2220
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
content-type: application/x-www-form-urlencoded
Referer: https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html
Accept-Encoding: gzip, deflate, br


url2    羽毛球选择场地和时间页面
GET https://mapv2.51yundong.me/api/stadium/resources/2c93809e821eb0ed01822a128aaf00b8/matrix?stadiumItemId=2c93809e821eb0ed01822a128aaf00b8&date=2022-08-22 HTTP/1.1
Host: mapv2.51yundong.me
Connection: keep-alive
Authorization: Bearer 600f48d7-89b6-4a7f-a5d4-ada10b2e2220
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
content-type: application/x-www-form-urlencoded
Referer: https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html
Accept-Encoding: gzip, deflate, br


url3    羽毛球下订单场地
POST https://mapv2.51yundong.me/api/order/orders?orderType=1 HTTP/1.1
Host: mapv2.51yundong.me
Connection: keep-alive
Content-Length: 503
Authorization: Bearer 600f48d7-89b6-4a7f-a5d4-ada10b2e2220
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
content-type: application/json
Referer: https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html
Accept-Encoding: gzip, deflate, br

{"app":"MAP","stadiumItemId":"2c93809e821eb0ed01822a128aaf00b8","stadiumId":"2c93809e821eb0ed01822a128aac00b7","details":[{"beginTime":"16:00","endTime":"17:00","fieldId":"1540192908268883969","fieldName":"三号场","resourceDate":"2022-08-22","amount":4000,"sessionId":"2022-08-22"},{"beginTime":"17:00","endTime":"18:00","fieldId":"1540193139911905282","fieldName":"九号场","resourceDate":"2022-08-22","amount":4000,"sessionId":"2022-08-22"}],"stadiumSource":"2022029","channel":1,"orderType":"1"}
'''

now = datetime.datetime.now()
delta = datetime.timedelta(days=2)
n_days = now + delta
print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d', time.localtime()))
