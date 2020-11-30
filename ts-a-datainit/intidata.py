import requests
import json
import random
import uuid
import datetime
import tornado.ioloop
import tornado.web


# 全部连接的admin
# login to get the token
url_getToken = 'http://ts-auth-service:12340/api/v1/users/login'

# create
url_createUser = 'http://ts-admin-user-service:16115/api/v1/adminuserservice/users'
# create connect
url_createConnect = 'http://ts-admin-basic-info-service:18767/api/v1/adminbasicservice/adminbasic/contacts'
# create inside_payment
url_createInside = 'http://ts-inside-payment-service:18673/api/v1/inside_pay_service/inside_payment/account'
''''''
# route control, get: get info, post: insert route
url_getrouteinfo= 'http://ts-admin-route-service:16113/api/v1/adminrouteservice/adminroute'
# get train info
url_train = 'http://ts-train-service:14567/api/v1/trainservice/trains'
# travel control, get: get info, post, add travel
url_travel = 'http://ts-admin-travel-service:16114/api/v1/admintravelservice/admintravel'
# create price
url_createPrice = 'http://ts-admin-basic-info-service:18767/api/v1/adminbasicservice/adminbasic/prices'


stations = [{'id': 'shanghai', 'name': 'Shang Hai', 'stayTime': 10}, {'id': 'shanghaihongqiao', 'name': 'Shang Hai Hong Qiao', 'stayTime': 10}, {'id': 'taiyuan', 'name': 'Tai Yuan', 'stayTime': 5}, {'id': 'beijing', 'name': 'Bei Jing', 'stayTime': 10}, {'id': 'nanjing', 'name': 'Nan Jing', 'stayTime': 8}, {'id': 'shijiazhuang', 'name': 'Shi Jia Zhuang', 'stayTime': 8}, {'id': 'xuzhou', 'name': 'Xu Zhou', 'stayTime': 7}, {'id': 'jinan', 'name': 'Ji Nan', 'stayTime': 5}, {'id': 'hangzhou', 'name': 'Hang Zhou', 'stayTime': 9}, {'id': 'jiaxingnan', 'name': 'Jia Xing Nan', 'stayTime': 2}, {'id': 'zhenjiang', 'name': 'Zhen Jiang', 'stayTime': 2}, {'id': 'wuxi', 'name': 'Wu Xi', 'stayTime': 3}, {'id': 'suzhou', 'name': 'Su Zhou', 'stayTime': 3}]
trains = [{'id': 'GaoTieOne', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 250}, {'id': 'GaoTieTwo', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 200}, {'id': 'DongCheOne', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 180}, {'id': 'ZhiDa', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 120}, {'id': 'TeKuai', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 120}, {'id': 'KuaiSu', 'economyClass': 50, 'confortClass': 50, 'averageSpeed': 90}]
routes = [{'id': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'stations': ['shanghai', 'nanjing', 'shijiazhuang', 'taiyuan'], 'distances': [0, 350, 1000, 1300], 'startStationId': 'shanghai', 'terminalStationId': 'taiyuan'}, {'id': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'stations': ['nanjing', 'xuzhou', 'jinan', 'beijing'], 'distances': [0, 500, 700, 1200], 'startStationId': 'nanjing', 'terminalStationId': 'beijing'}, {'id': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'stations': ['taiyuan', 'shijiazhuang', 'nanjing', 'shanghai'], 'distances': [0, 300, 950, 1300], 'startStationId': 'taiyuan', 'terminalStationId': 'shanghai'}, {'id': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'stations': ['shanghai', 'taiyuan'], 'distances': [0, 1300], 'startStationId': 'shanghai', 'terminalStationId': 'taiyuan'}, {'id': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'stations': ['shanghaihongqiao', 'jiaxingnan', 'hangzhou'], 'distances': [0, 150, 300], 'startStationId': 'shanghaihongqiao', 'terminalStationId': 'hangzhou'}, {'id': '92708982-77af-4318-be25-57ccb0ff69ad', 'stations': ['nanjing', 'zhenjiang', 'wuxi', 'suzhou', 'shanghai'], 'distances': [0, 100, 150, 200, 250], 'startStationId': 'nanjing', 'terminalStationId': 'shanghai'}, {'id': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'stations': ['nanjing', 'shanghai'], 'distances': [0, 250], 'startStationId': 'nanjing', 'terminalStationId': 'shanghai'}, {'id': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'stations': ['nanjing', 'suzhou', 'shanghai'], 'distances': [0, 200, 250], 'startStationId': 'nanjing', 'terminalStationId': 'shanghai'}, {'id': '084837bb-53c8-4438-87c8-0321a4d09917', 'stations': ['suzhou', 'shanghai'], 'distances': [0, 50], 'startStationId': 'suzhou', 'terminalStationId': 'shanghai'}, {'id': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'stations': ['shanghai', 'suzhou'], 'distances': [0, 50], 'startStationId': 'shanghai', 'terminalStationId': 'suzhou'}]


class Login:
    def __init__(self, username, password, ver):
        self.__url = url_getToken
        if ver == None:
            self.__data  = {"username": "admin", "password": "222222"}
        else:
            self.__data = {"username": username, "password": password, "verificationCode": ver}
        req = requests.post(self.__url, json=self.__data)
        self.__token = json.loads(req.text)['data']['token']


    def getHeaders(self):
        heads = {
            # 'Content-Type': 'applon/json',
            'Authorization': 'Bearer ' + self.__token
        }
        return heads


# create user, users' connect, users' inside_payment
def createUsersAndConnects():
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    for i in range(0, 1000):
        user_data = {
            # 'userId': uuid.uuid1(),
            'userName': 'microserivce_userName' + str(i),
            'password': '111111',
            'gender': random.randint(0, 1),
            'documentType': 1,
            'documentNum': str(int(random.random()*1000000)) + str(int(random.random()*10000000)) + 'X',
            'email': 'microserivce_userName' + str(i) + "@163.com"
        }
        print("%d 's people is registered", i)
        q = requests.post(url_createUser, json=user_data, headers=heads)
        q_data = json.loads(q.text)
        if json.loads(q.text)['status'] == 1:
            # 联系人生成
            connect_data = {
                'id' : str(uuid.uuid1()),
                'accountId' : q_data['data']['userId'],
                'name' : 'Contacts_One',
                'documentType' : 1,
                'documentNumber' : 'DocumentNumber_One',
                'phoneNumber' : 'ContactsPhoneNum_One'
            }
            q1 = requests.post(url_createConnect, json=connect_data, headers=heads)
            print("%d 's people's connect is registered", i)
            q1.close()
           # inside_payment生成
            inside_payment_data = {
                'userId' : q_data['data']['userId'],
                'money' : '10000',
            }
            q2 = requests.post(url_createInside, json=inside_payment_data, headers=heads)
            print("%d 's people's insidepayment is registered", i)
            q2.close()
            q.close()


travel_data = [{0: {'trip_data': {'loginId': 'admin', 'tripId': 'G839', 'trainTypeId': 'GaoTieTwo', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'startingStationId': 'shanghai', 'stationsId': "['shanghai', 'nanjing', 'shijiazhuang', 'taiyuan']", 'terminalStationId': 'shijiazhuang', 'startingTime': '2020-11-27T16:40:34.248232', 'endTime': '2020-11-27T21:40:34.248232'}, 'cost_time': 300}}, {1: {'trip_data': {'loginId': 'admin', 'tripId': 'G869', 'trainTypeId': 'GaoTieTwo', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'xuzhou', 'jinan', 'beijing']", 'terminalStationId': 'jinan', 'startingTime': '2020-11-27T18:40:34.248277', 'endTime': '2020-11-27T22:10:34.248277'}, 'cost_time': 210}}, {2: {'trip_data': {'loginId': 'admin', 'tripId': 'D943', 'trainTypeId': 'DongCheOne', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'startingStationId': 'xuzhou', 'stationsId': "['xuzhou', 'jinan']", 'terminalStationId': 'jinan', 'startingTime': '2020-11-27T18:40:34.248291', 'endTime': '2020-11-27T19:46:34.248291'}, 'cost_time': 66}}, {3: {'trip_data': {'loginId': 'admin', 'tripId': 'T123', 'trainTypeId': 'TeKuai', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'xuzhou', 'jinan']", 'terminalStationId': 'jinan', 'startingTime': '2020-11-27T17:40:34.248302', 'endTime': '2020-11-27T23:30:34.248302'}, 'cost_time': 350}}, {4: {'trip_data': {'loginId': 'admin', 'tripId': 'G674', 'trainTypeId': 'GaoTieTwo', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'startingStationId': 'shijiazhuang', 'stationsId': "['taiyuan', 'shijiazhuang', 'nanjing', 'shanghai']", 'terminalStationId': 'nanjing', 'startingTime': '2020-11-27T18:40:34.248313', 'endTime': '2020-11-27T21:55:34.248313'}, 'cost_time': 195}}, {5: {'trip_data': {'loginId': 'admin', 'tripId': 'K555', 'trainTypeId': 'KuaiSu', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'startingStationId': 'shijiazhuang', 'stationsId': "['shijiazhuang', 'nanjing', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T17:40:34.248323', 'endTime': '2020-11-28T04:46:34.248323'}, 'cost_time': 666}}, {6: {'trip_data': {'loginId': 'admin', 'tripId': 'G355', 'trainTypeId': 'GaoTieOne', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'startingStationId': 'shijiazhuang', 'stationsId': "['shijiazhuang', 'nanjing']", 'terminalStationId': 'nanjing', 'startingTime': '2020-11-27T17:40:34.248334', 'endTime': '2020-11-27T20:16:34.248334'}, 'cost_time': 156}}, {7: {'trip_data': {'loginId': 'admin', 'tripId': 'G423', 'trainTypeId': 'GaoTieOne', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'startingStationId': 'shanghai', 'stationsId': "['shanghai', 'taiyuan']", 'terminalStationId': 'taiyuan', 'startingTime': '2020-11-27T17:40:34.248344', 'endTime': '2020-11-27T22:52:34.248344'}, 'cost_time': 312}}, {8: {'trip_data': {'loginId': 'admin', 'tripId': 'Z423', 'trainTypeId': 'ZhiDa', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'startingStationId': 'shanghai', 'stationsId': "['shanghai', 'taiyuan']", 'terminalStationId': 'taiyuan', 'startingTime': '2020-11-27T17:40:34.248353', 'endTime': '2020-11-28T04:30:34.248353'}, 'cost_time': 650}}, {9: {'trip_data': {'loginId': 'admin', 'tripId': 'D142', 'trainTypeId': 'DongCheOne', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'startingStationId': 'shanghai', 'stationsId': "['shanghai', 'taiyuan']", 'terminalStationId': 'taiyuan', 'startingTime': '2020-11-27T18:40:34.248363', 'endTime': '2020-11-28T01:53:34.248363'}, 'cost_time': 433}}, {10: {'trip_data': {'loginId': 'admin', 'tripId': 'G702', 'trainTypeId': 'GaoTieOne', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'startingStationId': 'shanghaihongqiao', 'stationsId': "['shanghaihongqiao', 'jiaxingnan', 'hangzhou']", 'terminalStationId': 'hangzhou', 'startingTime': '2020-11-27T18:40:34.248374', 'endTime': '2020-11-27T19:52:34.248374'}, 'cost_time': 72}}, {11: {'trip_data': {'loginId': 'admin', 'tripId': 'D495', 'trainTypeId': 'DongCheOne', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'startingStationId': 'shanghaihongqiao', 'stationsId': "['shanghaihongqiao', 'jiaxingnan']", 'terminalStationId': 'jiaxingnan', 'startingTime': '2020-11-27T18:40:34.248383', 'endTime': '2020-11-27T19:30:34.248383'}, 'cost_time': 50}}, {12: {'trip_data': {'loginId': 'admin', 'tripId': 'G713', 'trainTypeId': 'GaoTieTwo', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'startingStationId': 'zhenjiang', 'stationsId': "['nanjing', 'zhenjiang', 'wuxi', 'suzhou', 'shanghai']", 'terminalStationId': 'wuxi', 'startingTime': '2020-11-27T18:40:34.248393', 'endTime': '2020-11-27T18:55:34.248393'}, 'cost_time': 15}}, {13: {'trip_data': {'loginId': 'admin', 'tripId': 'K58', 'trainTypeId': 'KuaiSu', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'zhenjiang', 'wuxi']", 'terminalStationId': 'wuxi', 'startingTime': '2020-11-27T18:40:34.248409', 'endTime': '2020-11-27T20:20:34.248409'}, 'cost_time': 100}}, {14: {'trip_data': {'loginId': 'admin', 'tripId': 'G48', 'trainTypeId': 'GaoTieOne', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'startingStationId': 'zhenjiang', 'stationsId': "['zhenjiang', 'wuxi', 'suzhou', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T17:40:34.248421', 'endTime': '2020-11-27T18:16:34.248421'}, 'cost_time': 36}}, {15: {'trip_data': {'loginId': 'admin', 'tripId': 'G721', 'trainTypeId': 'GaoTieTwo', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T18:40:34.248437', 'endTime': '2020-11-27T19:55:34.248437'}, 'cost_time': 75}}, {16: {'trip_data': {'loginId': 'admin', 'tripId': 'K674', 'trainTypeId': 'KuaiSu', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T17:40:34.248449', 'endTime': '2020-11-27T20:26:34.248449'}, 'cost_time': 166}}, {17: {'trip_data': {'loginId': 'admin', 'tripId': 'G871', 'trainTypeId': 'GaoTieOne', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T18:40:34.248459', 'endTime': '2020-11-27T19:40:34.248459'}, 'cost_time': 60}}, {18: {'trip_data': {'loginId': 'admin', 'tripId': 'D435', 'trainTypeId': 'DongCheOne', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'suzhou', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T18:40:34.248469', 'endTime': '2020-11-27T20:03:34.248469'}, 'cost_time': 83}}, {19: {'trip_data': {'loginId': 'admin', 'tripId': 'G355', 'trainTypeId': 'GaoTieOne', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'startingStationId': 'nanjing', 'stationsId': "['nanjing', 'suzhou']", 'terminalStationId': 'suzhou', 'startingTime': '2020-11-27T18:40:34.248479', 'endTime': '2020-11-27T19:28:34.248479'}, 'cost_time': 48}}, {20: {'trip_data': {'loginId': 'admin', 'tripId': 'Z5', 'trainTypeId': 'ZhiDa', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'startingStationId': 'suzhou', 'stationsId': "['suzhou', 'shanghai']", 'terminalStationId': 'shanghai', 'startingTime': '2020-11-27T18:40:34.248489', 'endTime': '2020-11-27T19:05:34.248489'}, 'cost_time': 25}}, {21: {'trip_data': {'loginId': 'admin', 'tripId': 'Z448', 'trainTypeId': 'ZhiDa', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'startingStationId': 'shanghai', 'stationsId': "['shanghai', 'suzhou']", 'terminalStationId': 'suzhou', 'startingTime': '2020-11-27T17:40:34.248499', 'endTime': '2020-11-27T18:05:34.248499'}, 'cost_time': 25}}]

price_train_route = [{'id': '426d9494-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.44, 'firstClassPriceRate': 1.0}, {'id': '426d9495-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.33, 'firstClassPriceRate': 1.0}, {'id': '426d9496-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.56, 'firstClassPriceRate': 1.0}, {'id': '426d9497-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.42, 'firstClassPriceRate': 1.0}, {'id': '426d9498-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.07, 'firstClassPriceRate': 1.0}, {'id': '426d9499-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '0b23bd3e-876a-4af3-b920-c50a90c90b04', 'basicPriceRate': 0.57, 'firstClassPriceRate': 1.0}, {'id': '426d949a-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.2, 'firstClassPriceRate': 1.0}, {'id': '426d949b-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.6, 'firstClassPriceRate': 1.0}, {'id': '426d949c-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.04, 'firstClassPriceRate': 1.0}, {'id': '426d949d-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.57, 'firstClassPriceRate': 1.0}, {'id': '426d949e-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.79, 'firstClassPriceRate': 1.0}, {'id': '426d949f-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '9fc9c261-3263-4bfa-82f8-bb44e06b2f52', 'basicPriceRate': 0.62, 'firstClassPriceRate': 1.0}, {'id': '426d94a0-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.65, 'firstClassPriceRate': 1.0}, {'id': '426d94a1-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.38, 'firstClassPriceRate': 1.0}, {'id': '426d94a2-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.96, 'firstClassPriceRate': 1.0}, {'id': '426d94a3-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.21, 'firstClassPriceRate': 1.0}, {'id': '426d94a4-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.92, 'firstClassPriceRate': 1.0}, {'id': '426d94a5-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': 'd693a2c5-ef87-4a3c-bef8-600b43f62c68', 'basicPriceRate': 0.63, 'firstClassPriceRate': 1.0}, {'id': '426d94a6-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.5, 'firstClassPriceRate': 1.0}, {'id': '426d94a7-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.95, 'firstClassPriceRate': 1.0}, {'id': '426d94a8-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.0, 'firstClassPriceRate': 1.0}, {'id': '426d94a9-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.73, 'firstClassPriceRate': 1.0}, {'id': '426d94aa-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.67, 'firstClassPriceRate': 1.0}, {'id': '426d94ab-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '20eb7122-3a11-423f-b10a-be0dc5bce7db', 'basicPriceRate': 0.9, 'firstClassPriceRate': 1.0}, {'id': '426d94ac-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.59, 'firstClassPriceRate': 1.0}, {'id': '426d94ad-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.57, 'firstClassPriceRate': 1.0}, {'id': '426d94ae-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.56, 'firstClassPriceRate': 1.0}, {'id': '426d94af-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.24, 'firstClassPriceRate': 1.0}, {'id': '426d94b0-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.78, 'firstClassPriceRate': 1.0}, {'id': '426d94b1-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '1367db1f-461e-4ab7-87ad-2bcc05fd9cb7', 'basicPriceRate': 0.92, 'firstClassPriceRate': 1.0}, {'id': '426d94b2-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.47, 'firstClassPriceRate': 1.0}, {'id': '426d94b3-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.4, 'firstClassPriceRate': 1.0}, {'id': '426d94b4-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.82, 'firstClassPriceRate': 1.0}, {'id': '426d94b5-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.17, 'firstClassPriceRate': 1.0}, {'id': '426d94b6-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.29, 'firstClassPriceRate': 1.0}, {'id': '426d94b7-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '92708982-77af-4318-be25-57ccb0ff69ad', 'basicPriceRate': 0.96, 'firstClassPriceRate': 1.0}, {'id': '426d94b8-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.01, 'firstClassPriceRate': 1.0}, {'id': '426d94b9-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.06, 'firstClassPriceRate': 1.0}, {'id': '426d94ba-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.72, 'firstClassPriceRate': 1.0}, {'id': '426d94bb-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.97, 'firstClassPriceRate': 1.0}, {'id': '426d94bc-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.46, 'firstClassPriceRate': 1.0}, {'id': '426d94bd-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': 'aefcef3f-3f42-46e8-afd7-6cb2a928bd3d', 'basicPriceRate': 0.86, 'firstClassPriceRate': 1.0}, {'id': '426d94be-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.29, 'firstClassPriceRate': 1.0}, {'id': '426d94bf-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.12, 'firstClassPriceRate': 1.0}, {'id': '426d94c0-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.52, 'firstClassPriceRate': 1.0}, {'id': '426d94c1-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.62, 'firstClassPriceRate': 1.0}, {'id': '426d94c2-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.67, 'firstClassPriceRate': 1.0}, {'id': '426d94c3-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': 'a3f256c1-0e43-4f7d-9c21-121bf258101f', 'basicPriceRate': 0.11, 'firstClassPriceRate': 1.0}, {'id': '426d94c4-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.74, 'firstClassPriceRate': 1.0}, {'id': '426d94c5-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.57, 'firstClassPriceRate': 1.0}, {'id': '426d94c6-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.19, 'firstClassPriceRate': 1.0}, {'id': '426d94c7-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.46, 'firstClassPriceRate': 1.0}, {'id': '426d94c8-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.99, 'firstClassPriceRate': 1.0}, {'id': '426d94c9-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': '084837bb-53c8-4438-87c8-0321a4d09917', 'basicPriceRate': 0.58, 'firstClassPriceRate': 1.0}, {'id': '426d94ca-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieOne', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.22, 'firstClassPriceRate': 1.0}, {'id': '426d94cb-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'GaoTieTwo', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.13, 'firstClassPriceRate': 1.0}, {'id': '426d94cc-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'DongCheOne', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.03, 'firstClassPriceRate': 1.0}, {'id': '426d94cd-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'ZhiDa', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.07, 'firstClassPriceRate': 1.0}, {'id': '426d94ce-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'TeKuai', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.76, 'firstClassPriceRate': 1.0}, {'id': '426d94cf-307d-11eb-9b8e-af7fe23a8d86', 'trainType': 'KuaiSu', 'routeId': 'f3d4d4ef-693b-4456-8eed-59c0d717dd08', 'basicPriceRate': 0.75, 'firstClassPriceRate': 1.0}]

# 与用户不同，火车路线服务尽量能够一直提供
def createTravelInfo():
    # in to controler
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    # 具体的思路为生成一天的铁路线路图，然后通过管理员在每天增加
    routesInfo = json.loads(requests.get(url_getrouteinfo, headers=heads).text)['data']
    trains = json.loads(requests.get(url_train, headers=heads).text)['data']
    h = 0
    for route in routesInfo:
        stations = route['stations']
        stations_num = len(stations)
        trip_nums = random.randint(1, 3)
        for j in range(trip_nums):
            choose = trains[random.randint(0, len(trains)-1)]
            startStation_num = random.randint(0, int(stations_num / 2) - 1)
            endStation_num = random.randint(int(stations_num / 2), stations_num - 1)
            # 计算车站
            stationsId = []
            if j != 0:
                for i in range(startStation_num, endStation_num+1):
                    stationsId.append(stations[i])
            else:
                stationsId = stations
            # 计算时间
            length = route['distances'][endStation_num] - route['distances'][startStation_num]
            cost_time = int(60 * length / choose['averageSpeed'])
            now = datetime.datetime.now()
            startTime = now + datetime.timedelta(hours=+random.randint(1, 3))
            endTime = startTime + datetime.timedelta(minutes=+cost_time)
            # str(time.strftime("%Y-%m-%dT%H:%M:%S", times)),
            # add travel
            trip_data = {
                'loginId': 'admin',
                'tripId': str(choose['id'])[0] + str(int(random.random()*1000)),
                'trainTypeId': choose['id'],
                'routeId': route['id'],
                'startingStationId': stations[startStation_num],
                'stationsId': str(stationsId),
                'terminalStationId': stations[endStation_num],
                'startingTime': str(startTime).replace(' ', 'T'),
                'endTime': str(endTime).replace(' ', 'T')
            }
            travel_data.append({h: {'trip_data': trip_data, 'cost_time': cost_time}})
            h = h+1
            # addTravel = requests.post(url_travel, headers=heads, json=trip_data)

def createPrice():
    # in to controler
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    # 具体的思路为生成一天的铁路线路图，然后通过管理员在每天增加
    routesInfo = json.loads(requests.get(url_getrouteinfo, headers=heads).text)['data']
    trains = json.loads(requests.get(url_train, headers=heads).text)['data']
    for route in routesInfo:
        for train in trains:
            price_data = {
                'id': str(uuid.uuid1()),
                'trainType': train['id'],
                'routeId': route['id'],
                'basicPriceRate': int(random.random() * 100) / 100,
                'firstClassPriceRate': 1.0
            }
            price_train_route.append(price_data)
            # add_price = requests.post(url_createPrice, headers=heads, json=price_data)
            # if json.loads(add_price.text)['status'] == 1:
            #     print(('%s 路线上， %s 火车创建成功').format(route['id'], train['id']))



# web app 创造travel
def createTravel():
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    h = 0
    for i in travel_data:
        trip_data = i[h]['trip_data']
        cost_time = i[h]['cost_time']
        h = h+1
        # 更改日期即可
        now = datetime.datetime.now()
        startTime = now + datetime.timedelta(hours=+random.randint(1, 3))
        endTime = startTime + datetime.timedelta(minutes=+cost_time)
        trip_data['startingTime'] = str(startTime).replace(' ', 'T')
        trip_data['endTime'] = str(endTime).replace(' ', 'T')
        # 添加行程
        addTravel = requests.post(url=url_travel, headers=heads, json=trip_data)

# web app创造 每个火车在每条路线上的价格
def create_price_train():
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    for i in price_train_route:
        add_price = requests.post(url_createPrice, headers=heads, json=i)


class InitDataUser(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("初始化user and connnects")
        createUsersAndConnects()
        print("初始化user成功")

class InitDataTravel(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("创造travel中")
        createTravel()
        print("创造travel成功")

class InitDataPrice(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("初始化price")
        create_price_train()
        print("初始化price成功")


def make_app():
    return tornado.web.Application([
        (r"/initDataUser", InitDataUser),
        (r"/initDataTravel", InitDataTravel),
        (r"/initDataPrice", InitDataPrice)
    ])

if __name__ == '__main__':
    # test()创建成功创建成功
    app = make_app()
    app.listen(18000)
    tornado.ioloop.IOLoop.current().start()