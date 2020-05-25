import requests
from requests.auth import HTTPBasicAuth
def test_oauth():
    r= requests.get(url="https://httpbin.testing-studio.com/basic-auth/banan/123",auth = HTTPBasicAuth("banan","123"))
    print(r)

