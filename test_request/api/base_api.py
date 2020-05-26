import requests


class BaseApi:
    def send_api(self,req:dict):
        #使用request完成多请求的改造（post，get,delete）,根据method动态改变
        return requests.request(**req).json()