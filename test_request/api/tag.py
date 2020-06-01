# -*- coding: utf-8 -*-
from pipes import Template
from string import Template

from test_request.api.base_api import BaseApi
from test_request.api.wework import WeWork


class Tag(BaseApi):
    secrete = '32TJe-1u9LUeUml4nVYiBA_3_etPFqA9ol16oP8dNtA'

    def __init__(self):
        self.token = WeWork().get_token(self.secrete)
    def add(self,**data):
        # data={
        #     "method":'post',
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        #     "params":{
        #         "access_token":self.token
        #     },
        #     "json":{
        #         "group_name": "test",
        #         "tag": [{
        #             "name": tag_name
        #         }
        #         ]
        #     }
        # }
        # data=self.load("../api/test_add.yaml")
        # data['params']['access_token'] = self.token
        # data['json']['tag'][0]['name']= tag_name
        #data=self.template('../api/test_add.yaml', {'token': self.token,'tag_name': tag_name})
        data.update({'token':self.token})
        data = self.template('../api/test_all.yaml',data,sub='get')
        return self.send_api(data)

    def get(self):
        # data = {
        #     "method":"post",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        #     "params": {
        #         "access_token": self.token
        #     },
        #     "json": {
        #         "tagid": []
        #     }
        # }
        data = self.load("../api/tag.get.yaml")
        data['params']['access_token']=self.token
        return self.send_api(data)

    def delete(self,tag_id):
        data={
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tagid": [
                    tag_id
                ]
            }
        }
        return self.send_api(data)


    def update(self,tag_id,name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?a",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id":tag_id,
                "name":name
            }
        }
        return self.send_api(data)