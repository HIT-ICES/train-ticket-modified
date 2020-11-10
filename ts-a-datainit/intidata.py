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

user_numbers = 0


class Login:
    def __init__(self, username, password, ver):
        self.__url = url_getToken
        if ver == None:
            self.__data  = {"username": "admin", "password": "222222"}
        else:
            self.__data = {"username": username, "password": password, "verificationCode": ver}
        req = requests.post(self.__url, json=self.__data, timeout=20)
        self.__token = json.loads(req.text)['data']['token']


    def getHeaders(self):
        heads = {
            # 'Content-Type': 'applon/json',
            'Authorization': 'Bearer ' + self.__token
        }
        return heads


# create user, users' connect, users' inside_payment
def createUsersAndConnects():
    global user_numbers
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    for i in range(user_numbers, user_numbers+100):
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
        q = requests.post(url_createUser, json=user_data, headers=heads, timeout=20)
        if json.loads(q.text)['status'] == 1:
            # 联系人生成
            connect_data = {
                'id' : str(uuid.uuid1()),
                'accountId' : json.loads(q.text)['data']['userId'],
                'name' : 'Contacts_One',
                'documentType' : 1,
                'documentNumber' : 'DocumentNumber_One',
                'phoneNumber' : 'ContactsPhoneNum_One'
            }
            requests.post(url_createConnect, json=connect_data, headers=heads, timeout=20)
            print("%d 's people's connect is registered", i)
           # inside_payment生成
            inside_payment_data = {
                'userId' : json.loads(q.text)['data']['userId'],
                'money' : '10000',
            }
            requests.post(url_createInside, json=inside_payment_data, headers=heads, timeout=20)
            print("%d 's people's insidepayment is registered", i)
    user_numbers = user_numbers + 100


# 与用户不同，火车路线服务尽量能够一直提供
def createTravelInfo():
    # in to controler
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    # 具体的思路为生成一天的铁路线路图，然后通过管理员在每天增加
    routesInfo = json.loads(requests.get(url_getrouteinfo, headers=heads).text)['data']
    trains = json.loads(requests.get(url_train, headers=heads).text)['data']
    for route in routesInfo:
        stations = route['stations']
        stations_num = len(stations)
        trip_nums = random.randint(3, 6)
        for j in range(trip_nums):
            choose = trains[random.randint(0, len(trains)-1)]
            startStation_num = random.randint(0, int(stations_num / 2) - 1)
            endStation_num = random.randint(int(stations_num / 2), stations_num - 1)
            # 计算车站
            stationsId = []
            for i in range(startStation_num, endStation_num+1):
                stationsId.append(stations[i])

            # 计算时间
            length = route['distances'][endStation_num] - route['distances'][startStation_num]
            cost_time = int(60 * length / choose['averageSpeed'])
            now = datetime.datetime.now()
            startTime = now + datetime.timedelta(hours=+random.randint(2, 12))
            endTime = startTime + datetime.timedelta(minutes=+cost_time)
            # str(time.strftime("%Y-%m-%dT%H:%M:%S", times)),

            # add travel
            trip_data={
                'loginId' : 'admin',
                'tripId' : str(choose['id'])[0] + str(int(random.random()*1000)),
                'trainTypeId': choose['id'],
                'routeId' : route['id'],
                'startingStationId' : stations[startStation_num],
                'stationsId' : str(stationsId),
                'terminalStationId' : stations[endStation_num],
                'startingTime' : str(startTime).replace(' ', 'T'),
                'endTime' : str(endTime).replace(' ', 'T')
            }
            addTravel = requests.post(url_travel, headers=heads, json=trip_data,timeout=20)

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
            add_price = requests.post(url_createPrice, headers=heads, json=price_data)
            if json.loads(add_price.text)['status'] == 1:
                print(('%s 路线上， %s 火车创建成功').format(route['id'], train['id']))


def test():
    adminLogin = Login('admin', '222222', None)
    heads = adminLogin.getHeaders()
    q = requests.get(url_travel, headers=heads, timeout=20)
    print(len(json.loads(q.text)['data']))



class InitDataUser(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        createUsersAndConnects()

class InitDataTravel(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        createTravelInfo()


class InitDataPrice(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        createPrice()


class Test(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = {'test':'success'}
        print(data)


def make_app():
    return tornado.web.Application([
        (r"/initDataUser", InitDataUser),
        (r"/initDataTravel", InitDataTravel),
        (r"/initDataPrice", InitDataPrice),
        (r"/test", Test)
    ])

if __name__ == '__main__':
    # test()创建成功创建成功
    app = make_app()
    app.listen(18000)
    tornado.ioloop.IOLoop.current().start()