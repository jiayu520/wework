# -*- coding: utf-8 -*-
from test_request.api.wework import WeWork


class TestWeWork:
    def test_get_token(self):
        secrete = '32TJe-1u9LUeUml4nVYiBA_3_etPFqA9ol16oP8dNtA'
        print(WeWork().get_token(secrete))


