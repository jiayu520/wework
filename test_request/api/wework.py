class WeWork(BaseApi):
    #获取token
    def get_token(self,secret):
        data = {
            "url":  'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params":{
                 "corpid":'ww7d5a0c948e0fcbbf',
                 "corpsecret":secret
          }
        }
