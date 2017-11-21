# 封装接口的方法
import requests

class RunRequests:
    def post_main(self,url=None,data=None):
        res = None
        #参数必须按照url、data顺序传入
        res = requests.post(url=url,data=data)
        print(res.text)
        print(res.encoding)
        return res


    def get_main(self,url=None,data=None):
        res = None
        #参数必须按照url、data顺序传入
        res = requests.get(url=url,data=data)
        print(res.text)
        return res

    #调用
    def run_m(self,method,url=None,data=None):
        res = None
        if method == 'Post':
            res = self.post_main(url,data)
        elif method == 'Get':
            res == self.get_main(url,data)
        else:
            print('不是Get或Post请求')
        return res

if __name__ == '__main__':
    data = {"username":"jack","password":"123","ImageCode":""}
    t = RunRequests()
    print(t.run_m('Get','http://192.168.0.106:8082/v1/login?'),data)
