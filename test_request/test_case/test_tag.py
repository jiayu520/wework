# -*- coding: utf-8 -*-
import json

import pytest

from test_request.api.base_api import BaseApi
from test_request.api.tag import Tag
import yaml

class TestTga:
    test_data = BaseApi.load("test_tag_data.yaml")
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        data = cls.tag.get()
        for name in ['add']:
            tag_id = cls.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                print(name)
                tag_id = tag_id[0]
                print(tag_id)
                cls.tag.delete(tag_id)
        #data = cls.tag.get()
        # for name in ['wangwu','hahaha']:
        #     tag_id = cls.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
        #     if tag_id:
        #        cls.tag.delete(tag_id[0])
    def setup(self):
        pass

    def test_get(self):
       assert self.tag.get()['errcode'] == 0
       #print(json.dumps(Tag().get(),indent=2))
        #print(Tag().add('hello'))


    @pytest.mark.parametrize("name_old,name_new",test_data)
    def test_all(self,name_old,name_new):
        data = self.tag.get()
        for name in [name_old, name_new]:
            tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
               print(name)
               tag_id=tag_id[0]
               print(tag_id)
               self.tag.delete(tag_id)
       # tag_id = self.tag.jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')
       # if tag_id:
       #     self.tag.delete(tag_id[0])
        assert self.tag.add(name_old)['errcode'] == 0
        tag_id = self.tag.jsonpath(self.tag.get(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update(tag_id,name_new)['errcode'] == 0

        # self.tag.get()
        # tags = self.tag.get()
        # if 'wangwu' in jsonpath(tags, '$..name'):
        #     self.tag.delete('wangwu')
        # #print(Tag().add())

    def test_add(self):
        assert self.tag.add("wanger")['errcode'] == 0

    def test_delete(self):
        print(Tag().delete())

    def test_update(self):
        print(Tag().update())