# @Time: 2022/8/20 23:26
# @Author: DoubleApple

import datetime
import requests
import json

# authorization = input("输入用户authorization: ")
# date = input("输入预订日期(%Y-%m-%d): ")
authorization = ''
date = ''
stadiumItem = ''
stadiumItemId = ''
headers = {}
headers_order = {}

stadium_mp = {
    '羽毛球': '2c93809e821eb0ed01822a128aaf00b8',
    '台球': '2c93809e821eb0ed01822a128abb00ba'
}


def init_header():
    global headers, headers_order
    headers = {
        'Host': 'mapv2.51yundong.me',
        'Connection': 'keep-alive',
        'Authorization': authorization,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/x-www-form-urlencoded',
        'Referer': 'https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    headers_order = {
        'Host': 'mapv2.51yundong.me',
        'Connection': 'keep-alive',
        'Authorization': authorization,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx8b97e9b9a6441e29/164/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }


def get_info(info_auth, info_date, type1):
    global authorization, date, stadiumItem, stadiumItemId
    authorization = info_auth
    date = info_date
    stadiumItem = type1
    stadiumItemId = stadium_mp[str(type1)]
    init_header()


def get_all_date():
    url = "https://mapv2.51yundong.me/api/stadium/resources/" + stadiumItemId + "/dates?stadiumItemId=" + stadiumItemId
    print("get_all_date -》 访问url：显示日期页面：\n" + url)
    response = requests.get(url=url, headers=headers)
    json_text = response.json()
    return json_text


def get_all_stadium():
    url = "https://mapv2.51yundong.me/api/stadium/resources/" + stadiumItemId + "/matrix?stadiumItemId=" + stadiumItemId + "&date=" + date
    print("get_all_stadium -》 访问url：显示" + stadiumItem + "场地页面：\n" + url)
    response = requests.get(url=url, headers=headers)
    json_text = response.json()
    return json_text


'''
抢两天后的场地 返回日期字符串
'''


def get_order_date():
    dis = datetime.timedelta(days=2)
    now = datetime.datetime.now()
    order_date = now + dis
    order_date = order_date.strftime('%Y-%m-%d')
    return order_date


def find_free_field():
    print("get_order_date -》 查找可以下单的场地")
    all_json = get_all_stadium()  # json格式
    data_list = all_json.get('data')
    requests_json = {}
    details = []
    for field_dic in data_list:  # dic： {fieldId,fieldName,fieldResource}
        for info_dic in field_dic.get('fieldResource'):
            # print(info_dic)
            info_time = info_dic.get('start')  # 19:00  ->  1140
            info_status = info_dic.get('status')
            field_filedName = field_dic.get('fieldName')
            # if info_status == 'FREE' and info_time == 1140:
            # if info_status == 'LOCKED' and info_time == 1140:
            if info_status == 'FREE' and info_time == 1140:  # 16*6 = 960
                detail = {}
                amount = info_dic.get('price')
                beginTime = str(int(info_time / 60)) + ":00"
                endTime = str(int(info_time / 60 + 1)) + ":00"
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
    # requests_json["stadiumItemId"] = "2c93809e821eb0ed01822a128aaf00b8"     # 球类型 :  羽毛
    requests_json["stadiumItemId"] = stadiumItemId  # 台球：
    requests_json["stadiumId"] = "2c93809e821eb0ed01822a128aac00b7"  # 体育馆号
    requests_json["details"] = details
    requests_json["stadiumSource"] = "2022029"  # 未知
    requests_json["channel"] = 1
    requests_json["orderType"] = "1"
    print("有" + str(len(details)) + "个" + stadiumItem + "场地")
    return requests_json


def kill_order():
    requests_json = find_free_field()
    json_str = json.dumps(requests_json, ensure_ascii=False)
    print(json_str)
    url = "https://mapv2.51yundong.me/api/order/orders?orderType=1"
    response = requests.request(method="POST", url=url, headers=headers_order, data=json_str.encode("UTF-8"))
    data_json = response.json()
    result = show_result_field(data_json)
    return result


## 拿到的球场
def show_result_field(raw_json):
    result = []
    for info_dic in raw_json.get('data').get('details'):
        sing_res = {}
        sing_res['type'] = stadiumItem
        sing_res['fieldName'] = info_dic['fieldName']
        sing_res['amount'] = info_dic['amount']
        sing_res['beginTime'] = info_dic['resourceDate'] + ' ' + info_dic['beginTime']
        result.append(sing_res)
    return result


# 实现GUI界面+exe文件
# if __name__ == "__main__":
    # print(get_all_date())

    # print(authorization, date)
    # print(headers)
    # print(get_all_stadium())
    # print(get_order_date())
    # print(find_free_field())
    # print(get_order_date())

    # # 第一步 注入信息
    # get_info('Bearer 6f44a5be-ede1-4893-a295-17727c058c97', '2022-08-26', '台球')
    # print(get_all_stadium())
    # # 第二部 下单
    # print(kill_order())
