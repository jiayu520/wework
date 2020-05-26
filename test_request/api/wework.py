import requests

from test_request.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid='ww7d5a0c948e0fcbbf'
    #获取token
    def get_token(self,secrete):
        data = {
            "method":"get",
            "url":  'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params":{
                 "corpid":self.corpid,
                 "corpsecret":secrete
          }
        }
        return self.send_api(data)['access_token']
