import requests


class Company(object):
    def __init__(self):
        super(Company, self).__init__()
        self.base_url = 'http://192.168.10.167:6609/windelephant/api/company/'
        self.headers = {
            'authorization': '941c825b67e4377036ad6e4314f04dbba952c2c800150afa10b07924ba2a1b8d'
        }

    def create(self):
        url = self.base_url + 'create'
        data0 = {
            'companyName': '修炼科技',
            'socialCode': 'xiulianzone',
            'abbreviation': '修炼',
            # 'superiorCompany': '',
            'licenseNo': 'xiulianlicense'
        }
        data1 = {
            'companyName': '中国联通',
            'socialCode': 'zhongguoliantong',
            'abbreviation': '中国联通',
            'superiorCompanyId': '59c86e31d9932e379c4e3b1f',
            'licenseNo': '123zhongguoliantong'
        }
        data2 = {
            'companyName': '江苏联通',
            'socialCode': 'jiangsuliantong',
            'abbreviation': '江苏联通',
            'superiorCompanyId': '59c22724fd2970216001461d',
            'licenseNo': '123江苏liantong'
        }
        data3 = {
            'companyName': '珠海联通',
            'socialCode': 'zhuhailiantong',
            'abbreviation': '珠海联通',
            'superiorCompanyId': '59c22731fd2970216001461f',
            'licenseNo': '123珠海liantong'
        }
        r = requests.post(url,data1, headers=self.headers)
        print(r.text)

    def updated(self):
        url = self.base_url + 'update'
        data = {

        }

    def delete(self):
        url = self.base_url + 'delete'
        data = {
            'id': '59bf936345fdbe2670af304b'
        }
        r = requests.post(url,data,headers=self.headers)
        print(r.text)

    def list(self):
        url = self.base_url + 'list'
        query = {
            'abbreviation': '联通'
        }
        r = requests.get(url,params=query,headers=self.headers)
        print(r.text)

    def tree_list(self):
        url = self.base_url + 'list/tree'
        query = {
            # 'company': '59c3818d58bb622fc010365d'
        }
        r = requests.get(url, params=query, headers=self.headers)
        print(r.text)

class Alarm(object):
    def __init__(self):
        super(Alarm, self).__init__()
        self.base_url = 'http://192.168.10.167:6609/windelephant/api/alarmSetting/'
        self.headers = {
            'authorization': 'df8916b628f72ead956bdd3667ca4764defae924f8f861ddfe3c16331eae3d0b'
        }

    def create(self):
        url = self.base_url + 'create'
        data = {
            'alarmName': 'test1', # 报警名称，string
            'alarmType': '禁行报警',    # 报警类型,string
            'beginTime': '2017-09-25 17:31', #开始时间
            'endTime': '2017-09-25 17:35',  # 结束时间
            'totalTime': '2',# 总时间
            # 'speedingValue': '55',  # 超速阈值
            'companyId': ['59c87412aec05b308c57cf5d'],  # 此报警策略的关联公司
        }
        r = requests.post(url,data,headers=self.headers)
        print(r.text)

    def remove(self):
        url = self.base_url + 'delete'
        data = {
            'IDList': []
        }

    def list(self):
        url = self.base_url + 'list'
        params = {
            # 'alarmType': '禁行报警',
            'companyId': '59c87412aec05b308c57cf5d'
        }
        r = requests.get(url,params=params,headers=self.headers)
        print(r.text)

if __name__ == '__main__':
    # d = Driver()
    # d.main()
    c = Company()
    c.tree_list()
    # a = Alarm()
    # a.list()