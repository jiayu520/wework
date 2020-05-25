import requests
def test_demo():
    url  = 'http://httpbin.testing-studio.com/cookies'
    header =  {"Cookie": "hogwarts=school"}
    r= requests.get(url=url,headers = header)
    print(r.request.headers)


def test_demo1():
    url  = 'http://httpbin.testing-studio.com/cookies'
    header =  {
        "User-Agent": "hogwarts=school"
    }
    cookie_data = {"yu":"jia"}
    r= requests.get(url=url,headers = header,cookies = cookie_data)
    print(r.request.headers)