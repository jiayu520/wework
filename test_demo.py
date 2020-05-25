import requests
from jsonpath import jsonpath
from hamcrest import *

class Test_Demo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "jiayu"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        # print(type(r))
        print(r.json())
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "jiayu"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        # print(type(r))
        # assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "jiayu"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        print(type(r))
        assert r.status_code == 200


    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        assert jsonpath(r.json(),'$..name')[0] == '霍格沃兹测试学院公众号'


    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'] ,equal_to('霍格沃兹测试学院公众号'))
