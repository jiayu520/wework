# -*- coding: utf-8 -*-
import json

from jsonpath import jsonpath

from test_request.api.tag import Tag


class TestTga:
    def setup(self):
        self.tag = Tag()

    def test_get(self):
       print(json.dumps(Tag().get(),indent=2))
        #print(Tag().add('hello'))

    def test_all(self):
       tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')
       if not tag_id:
           self.tag.delete(tag_id[0])
       self.tag.add('wangwu')
       tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')[0]
       self.tag.update(tag_id,'haha')

        # self.tag.get()
        # tags = self.tag.get()
        # if 'wangwu' in jsonpath(tags, '$..name'):
        #     self.tag.delete('wangwu')
        # #print(Tag().add())

    def test_delete(self):
        print(Tag().delete())

    def test_update(self):
        print(Tag().update())