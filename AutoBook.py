# @Time: 2022/8/20 23:26
# @Author: DoubleApple

import datetime
import requests
import json

authorization = 'Bearer 8a69c702-3198-4954-a472-9b118f860b5f'

headers = {
    'Host': 'mapv2.51yundong.me',
    'Connection': 'keep-alive',
    # 号1
    'Authorization': authorization,
    # 号2
    # 'Authorization': 'Bearer a37ca078-30c9-439c-a630-04420ccd6ac8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/x-www-form-urlencoded',
    'Referer': 'https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}

headers_order = {
    'Host': 'mapv2.51yundong.me',
    'Connection': 'keep-alive',
    # 号1
    'Authorization': authorization,
    # 号2
    # 'Authorization': 'Bearer a37ca078-30c9-439c-a630-04420ccd6ac8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}

def get_all_date():
    url = "https://mapv2.51yundong.me/api/stadium/resources/2c93809e821eb0ed01822a128aaf00b8/dates?stadiumItemId=2c93809e821eb0ed01822a128aaf00b8"
    print("访问url：显示日期页面：\n"+url)
    response = requests.get(url=url, headers=headers)
    json_text = response.json()
    print(json_text)


def get_all_stadium():
    order_date = get_order_date()
    url = "https://mapv2.51yundong.me/api/stadium/resources/2c93809e821eb0ed01822a128aaf00b8/matrix?stadiumItemId=2c93809e821eb0ed01822a128aaf00b8&date=" + order_date
    print("访问url：显示场地页面：\n"+url)
    response = requests.get(url=url, headers=headers)
    json_text = response.json()
    return json_text


'''
抢两天后的场地 返回日期字符串
'''


def get_order_date():
    dis = datetime.timedelta(days=1)
    now = datetime.datetime.now()
    order_date = now + dis
    order_date = order_date.strftime('%Y-%m-%d')
    return order_date


def find_free_field():
    all_json = get_all_stadium()    #  json格式
    data_list = all_json.get('data')
    requests_json = {}
    details = []
    for field_dic in data_list:  # dic： {fieldId,fieldName,fieldResource}
        for info_dic in field_dic.get('fieldResource'):
            # print(info_dic)
            info_time = info_dic.get('start')   # 19:00  ->  1140
            info_status =  info_dic.get('status')
            field_filedName = field_dic.get('fieldName')
            # print(field_filedName)
            # if info_time == 1140:
            #     print(info_dic)
            # if info_status == 'FREE' and info_time == 1140:
            # if info_status == 'LOCKED' and info_time == 1140:
            if info_status == 'FREE' and info_time == 960 and field_filedName == "九号场":     # 16*6 = 960

                detail = {}

                amount = info_dic.get('price')
                beginTime = str(int(info_time/60)) + ":00"
                endTime = str(int(info_time/60+1)) + ":00"
                fieldId = field_dic.get('fieldId')
                fieldName = field_dic.get('fieldName')
                resourceDate = info_dic.get('recordId')
                sessionId = info_dic.get('recordId')

                detail["beginTime"] = beginTime
                detail["endTime"] = endTime
                detail["fieldId"] = fieldId
                detail["fieldName"] = fieldName
                detail["resourceDate"] = resourceDate
                detail["amount"] = int(amount)
                detail["sessionId"] = sessionId
                if len(details) < 2:
                    details.append(detail)
                # print(detail)
    requests_json["app"] = "MAP"
    requests_json["stadiumItemId"] = "2c93809e821eb0ed01822a128aaf00b8"     # 球类型
    requests_json["stadiumId"] = "2c93809e821eb0ed01822a128aac00b7"     # 体育馆号
    requests_json["details"] = details
    requests_json["stadiumSource"] = "2022029"  # 未知
    requests_json["channel"] = 1
    requests_json["orderType"] = "1"
    # field_name = data_list[0].get('fieldName')
    # print(field_name)
    print("有" + str(len(details)) + "个场地")
    # print(requests_json)
    return requests_json

def find_free_field_test():
    detail = {}
    details = []
    requests_json = {}
    detail["beginTime"] = "16:00"
    detail["endTime"] = "17:00"
    detail["fieldId"] = "1540193139911905282"
    detail["fieldName"] = "九号场"
    detail["resourceDate"] = "2022-08-22"
    detail["amount"] = 4000
    detail["sessionId"] = "2022-08-22"
    details.append(detail)

    # print(detail)
    requests_json["app"] = "MAP"
    requests_json["stadiumItemId"] = "2c93809e821eb0ed01822a128aaf00b8"  # 球类型
    requests_json["stadiumId"] = "2c93809e821eb0ed01822a128aac00b7"  # 体育馆号
    requests_json["details"] = details
    requests_json["stadiumSource"] = "2022029"  # 未知
    requests_json["channel"] = 1
    requests_json["orderType"] = "1"
    return requests_json


def kill_order():
    # requests_json = find_free_field_test()
    # json_str = json.dumps(requests_json, ensure_ascii=False)
    # print(json_str)

    requests_json2 = find_free_field()
    json_str2 = json.dumps(requests_json2, ensure_ascii=False)
    print(json_str2)
    url = "https://mapv2.51yundong.me/api/order/orders?orderType=1"
    response = requests.request(method="POST", url=url, headers=headers_order, data=json_str2.encode("UTF-8"))
    data_json = response.json()
    print(data_json)

    return 1


if __name__ == "__main__":
    # get_all_date()
    # print(get_all_stadium())
    # print(get_order_date())
    # print(find_free_field())
    print(kill_order())

