from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath

class BaseApi:
    def send_api(self, req: dict):
        # 使用request完成多请求的改造（post，get,delete）,根据method动态改变
        pprint(req)
        r=requests.request(**req)
        pprint(r.json())
        return r.json()
        #return requests.request(**req).json()
    @classmethod
    def jsonpath(cls,json,expr):
        return jsonpath(json,expr)

    @classmethod
    def load(cls,path):
        with open(path, 'r') as f:
             return (yaml.safe_load(f))

    @classmethod
    def template(cls,path,data,sub=None):
        with open(path,'r') as f:
            if sub is None:
               return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                return yaml.load(Template(yaml.dump(yaml.load(f)[sub])).substitute(data))
                #return yaml.safe_load(Template(f.read()).substitute(data))[sub]